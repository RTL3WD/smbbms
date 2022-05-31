from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from .contact import Contact

import stripe

class EmailAdmin(admin.ModelAdmin):
    # list_filter = ['name']
    list_display = ['id','email']
    search_fields = ['id','email']

class EmailAddress(models.Model):

    email_choices = (
        ("primary","Primary"),
        ("secondary","Secondary"),
    )

    email = models.CharField(max_length=300)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=email_choices)

@receiver(pre_save, sender=EmailAddress)
def update_stripe_email_addresses(sender, instance, **kwargs):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    customer = stripe.Customer.retrieve(instance.contact.stripe_customer_identifier)

    try:
        email_addresses = customer['metadata']['Email Addresses']
    except:
        email_addresses = ""

    if email_addresses == "":
        email_addresses = instance.email
    if email_addresses != "":
        if instance.email in email_addresses:
            email_addresses = email_addresses
        if instance.email not in email_addresses:
            email_addresses = instance.email + " " + email_addresses

    if instance.type == "primary":
        stripe.Customer.modify(
            customer.id,
            email=instance.email,
            metadata={"Email Addresses": email_addresses},
        )
    else:
        stripe.Customer.modify(
            customer.id,
            metadata={"Email Addresses": email_addresses},
        )

@receiver(pre_delete, sender=EmailAddress)
def delete_stripe_email_addresses(sender, instance, **kwargs):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    customer = stripe.Customer.retrieve(instance.contact.stripe_customer_identifier)

    email = str(instance.email)

    try:
        email_addresses = customer['metadata']['Email Addresses']
    except:
        email_addresses = ""

    if email != "":
        if email + " " in email_addresses:
            email_addresses = email_addresses.replace(email + " ", "")
        if email in email_addresses:
            email_addresses = email_addresses.replace(email, "")
        
        stripe.Customer.modify(
            customer.id,
            metadata={"Email Addresses": email_addresses},
        )