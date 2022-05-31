from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import pre_save
from django.dispatch import receiver

import stripe

# Create your models here.

class Contact(models.Model):

    contact_type_choices = (
        ('customer','Customer'),
        ('prospect','Prospect'),
        ('third_party','Third Party'),
    )

    gender_choices = (
        ('male','Male'),
        ('female','Female'),
    )
        
    # Primary Fields 
    # Contact Type
    contact_type = models.CharField(max_length=200,choices=contact_type_choices)
    # Contact First Name, Required Field
    first_name = models.CharField(max_length=200,blank=True)
    # Contact Middle Name
    middle_name = models.CharField(max_length=200,blank=True)
    # Contact Last Name, Required Field
    last_name = models.CharField(max_length=200,blank=True)
    # Contact's age
    date_of_birth = models.DateField(blank=True,null=True)
    # Contact's gender
    gender = models.CharField(max_length=200,choices=gender_choices,blank=True)

    # Stripe ID
    stripe_customer_identifier = models.CharField(max_length=200,blank=True)

    # Methods
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}' if self.middle_name != '' else f'{self.first_name} {self.last_name}'

# @receiver(pre_save, sender=Contact)
# def create_stripe_customer(sender, instance, **kwargs):
#     if instance.stripe_customer_identifier == "":
#         try:
#             stripe.api_key = settings.STRIPE_SECRET_KEY

#             fname = instance.first_name
#             mname = instance.middle_name
#             lname = instance.last_name

#             name = f'{fname} {mname} {lname}' if mname != '' else f'{fname} {lname}'
        
#             customer = stripe.Customer.create(
#                 name=name,
#             )

#             instance.stripe_customer_identifier = customer.id
#             print(f'SUCCESS:{fname} {lname} has been created in stripe as {customer.id}')
#         except:
#             print(f'FAILED:{instance.first_name} {instance.last_name} was not created in stripe.')
#             quit()