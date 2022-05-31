from django.forms import model_to_dict
from contacts.models import Contact
from django.contrib import admin
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver

import stripe

from products.models.product import Product

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
    products = models.ManyToManyField(Product,blank=True)
    subtotal = models.DecimalField(decimal_places=2,max_digits=7,blank=True,null=True)
    charge_amount = models.DecimalField(decimal_places=2,max_digits=7,blank=True,null=True)
    stripe_charge_identifier = models.CharField(max_length=200,blank=True)
    refund_amount = models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    stripe_refund_identifier = models.CharField(max_length=200,blank=True)
    last_modified_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.stripe_refund_identifier != '':
            return "REFUND: $" + str(self.charge_amount) + " " + str(self.stripe_refund_identifier)
        else:
            return "CHARGE: $" + str(self.charge_amount) + " " + str(self.stripe_charge_identifier)



# @receiver(m2m_changed, sender=Transaction.products.through)
# def subtract_subtotal( sender, instance, action="post_add", **kwargs):
#     print(instance.subtotal)

@receiver(m2m_changed, sender=Transaction.products.through)
def add_subtotal( sender, instance, action, **kwargs):
        subtotal = 0
        instance = model_to_dict(instance)
        print(instance)

        for product in instance['products']:
            try:
                subtotal = subtotal + product.price
            except:
                subtotal = subtotal + 0
        print(subtotal)
        instance['subtotal'] = subtotal
        # subtotal = instance.subtotal
   

@receiver(pre_save, sender=Transaction)
def stripe_transaction(sender, instance, **kwargs):
    stripe.api_key = "sk_test_w6mwZGryUkTVOvRCA0se0cGw"

    if instance.type == "charge" and instance.stripe_charge_identifier == '':

        # Convert decimal string to integer amount
        string_amount = str(instance.charge_amount)
        replaced_string_amount = string_amount.replace(".","")
        int_amount = int(replaced_string_amount)   

        # print(string_amount)
        # print(replaced_string_amount)
        # print(int_amount)   
        
        # Create charge
        stripe_charge = stripe.Charge.create(
        amount=int_amount,
        currency="usd",
        source="tok_visa",
        description="My First Test Charge (created for API docs)",
        )

        instance.charge_amount = string_amount
        instance.stripe_charge_identifier = stripe_charge.id
        instance.type = "charge"

    elif instance.type == "refund" or instance.type == "partial_refund" and instance.stripe_refund_identifier == '':

        if instance.refund_amount != None:
            # Convert decimal string to integer amount
            string_amount = str(instance.refund_amount)
            replaced_string_amount = string_amount.replace(".","")
            int_amount = int(replaced_string_amount)

            # Create Partial Refund
            refund = stripe.Refund.create(amount = int_amount, charge = instance.stripe_charge_identifier)

            # Update Transaction
            instance.type = "partial_refund"
            instance.stripe_refund_identifier = refund.id

        else:
            # Create Full Refund
            refund = stripe.Refund.create(charge = instance.stripe_charge_identifier)

            # Update Transaction Type
            instance.type = "refund"
            instance.stripe_refund_identifier = refund.id
            instance.refund_amount = instance.charge_amount
    else:
        pass

class TransactionAdmin(admin.ModelAdmin):

    # list_filter = ['name']
    list_display = ['created_date_time','id','type','contact__first_name contact__last_name','stripe_charge_identifier','stripe_refund_identifier','last_modified_date_time']
    search_fields = ['created_date_time','id','type','contact__first_name contact__last_name']