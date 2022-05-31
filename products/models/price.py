from django.conf import settings
from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .product import Product

import stripe

# Create your models here.

class PriceAdmin(admin.ModelAdmin):
    list_display = ['product','amount','billing_scheme',]
    search_fields = ['product__name','product__sku','amount']

class Price(models.Model):

    billing_choices = (
        ("per_unit","Per Unit"),
        ("tiered","Tiered"),
    )

    currency_choices = (
        ("usd","United States Dollar ($)"),
    )

    amount = models.DecimalField(max_digits=6,decimal_places=2)
    billing_scheme = models.CharField(max_length=30,blank=True,choices=billing_choices,default="per_unit",null=True)
    currency = models.CharField(choices=currency_choices,default="usd",max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_identifier = models.CharField(max_length=27,blank=True,null=True)

    def __str__(self) -> str:
        return f"${self.amount}"

@receiver(pre_save, sender=Price)
def create_stripe_price(sender, instance, **kwargs):
  if instance.stripe_price_identifier == None:
      stripe.api_key = settings.STRIPE_SECRET_KEY
      product_id = instance.product_id
      product = Product.objects.get(pk=product_id)
      stripe_product_identifier = product.stripe_product_identifier
      # Convert decimal string to integer amount
      string_amount = str(instance.amount)
      replaced_string_amount = string_amount.replace(".","")
      int_amount = int(replaced_string_amount)   
      
      # Create price
      price = stripe.Price.create(
          unit_amount=int_amount,
          currency="usd",
          product=stripe_product_identifier,
      )
      instance.stripe_price_identifier = price.id