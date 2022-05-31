from django.forms import model_to_dict
from django.contrib import admin
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver

import stripe

from contacts.models.contact import Contact
from products.models.product import Product

# Create your models here.

class InvoiceItem(models.Model):
    # CHOICES

    # FIELDS
    customer = models.ForeignKey(Contact, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # MANAGERS

    # META

    # DEF __STR__()
    def __str__(self) -> str:
        return super().__str__()

    # DEF SAVE()

    # DEF GET_ABSOLUTE_URL()

    # CUSTOM METHODS

    def finalize(self):

        customer = self.customer
        print(customer)

        # stripe.InvoiceItem.create(
        #     customer = customer,
        #     price = "price_1KUG8ZJ7cpQFgDDPL8ZeOGOO",
        # )