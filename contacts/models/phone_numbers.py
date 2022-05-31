from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from .contact import Contact
from phone_field import PhoneField

import stripe

# TODO:
# make sure stripe properly updates customer phone number information
# 
# 
# 
# FIXME:
# 
# 
# 
# 
# 



class PhoneAdmin(admin.ModelAdmin):
    # list_filter = ['name']
    list_display = ['id','phone_number']
    search_fields = ['id','phone_number']

class PhoneNumber(models.Model):

    phone_choices = (
        ("primary","Primary"),
        ("secondary","Secondary"),
    )

    phone_number = PhoneField(help_text='Enter numbers only')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=phone_choices)

    def __str__(self) -> str:
        return f'{self.contact} | {self.phone_number}'

# @receiver(pre_save, sender=PhoneNumber)
# def update_stripe_phone_numbers(sender, instance, **kwargs):
#         stripe.api_key = settings.STRIPE_SECRET_KEY

#         customer = stripe.Customer.retrieve(instance.contact.stripe_customer_identifier)

#         try:
#             phone_numbers = customer['metadata']['Phone Numbers']
#         except:
#             phone_numbers = ""
        
#         phone = str(instance.phone_number)

#         if phone_numbers == "":
#             phone_numbers = phone
#         if phone_numbers != "":
#             if phone in phone_numbers:
#                 phone_numbers = phone_numbers
#             if phone not in phone_numbers:
#                 phone_numbers = phone + " " + phone_numbers

#         if instance.type == "primary":
#             stripe.Customer.modify(
#                 customer.id,
#                 phone=phone,
#                 metadata={"Phone Numbers": phone_numbers},
#             )
#         else:            
#             stripe.Customer.modify(
#                 customer.id,
#                 metadata={"Phone Numbers": phone_numbers},
#             )


# @receiver(pre_delete, sender=PhoneNumber)
# def delete_stripe_phone_numbers(sender, instance, **kwargs):
#     stripe.api_key = settings.STRIPE_SECRET_KEY

#     customer = stripe.Customer.retrieve(instance.contact.stripe_customer_identifier)

#     phone = str(instance.phone_number)

#     try:
#         phone_numbers = customer['metadata']['Phone Numbers']
#     except:
#         phone_numbers = ""

#     if phone != "":
#         if phone + " " in phone_numbers:
#             phone_numbers = phone_numbers.replace(phone + " ", "")
#         if phone in phone_numbers:
#             phone_numbers = phone_numbers.replace(phone, "")
        
#         stripe.Customer.modify(
#             customer.id,
#             metadata={"Phone Numbers": phone_numbers},
#         )