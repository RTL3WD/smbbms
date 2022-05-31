from tkinter import CASCADE
from contacts.models import Contact
from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import stripe

from products.models.product2 import Product

# Create your models here.

class Transaction(models.Model):

    # Transaction Choices
    transaction_choices = (
        ('partial_refund','Partial Refund'),
        ('proposal','Proposal'),
        ('pending','Pending'),
        ('invoice','Invoice'),
        ('charge','Charge'),
        ('refund','Refund'),
        ('subscription','Subscription'),
        ('quote','Quote'),
    )

    created_date_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=15,blank=True,choices=transaction_choices)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    charge_amount = models.DecimalField(decimal_places=2,max_digits=7,blank=True)
    stripe_charge_identifier = models.CharField(max_length=200,blank=True)
    refund_amount = models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    stripe_refund_identifier = models.CharField(max_length=200,blank=True)
    last_modified_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.stripe_refund_identifier != '':
            return "REFUND: $" + str(self.charge_amount) + " " + str(self.stripe_refund_identifier)
        else:
            return "CHARGE: $" + str(self.charge_amount) + " " + str(self.stripe_charge_identifier)

@receiver(pre_save, sender=Transaction)
def stripe_transaction(sender, instance, **kwargs):
    

    pass
    
class TransactionAdmin(admin.ModelAdmin):

    # list_filter = ['name']
    list_display = ['created_date_time','id','type','contact__first_name contact__last_name','stripe_charge_identifier','stripe_refund_identifier','last_modified_date_time']
    search_fields = ['created_date_time','id','type','contact__first_name contact__last_name']