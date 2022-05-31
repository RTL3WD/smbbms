from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import stripe


# Create your models here.

class Product(models.Model):

  uom_len_choices = (
    ('millimeters','Millimeters'),
    ('centimeters','Centimeters'),
    ('inches','Inches'),
    ('feet','Feet'),
    ('meters','Meters'),
    ('yards','Yards'),
  )

  uom_mass_choices = (
    ('milligrams','Milligrams'),
    ('grams','Grams'),
    ('ounces','Ounces'),
    ('pounds','Pounds'),
  )


  created_date_time = models.DateTimeField(auto_now_add=True)

  sku = models.CharField(max_length=200,blank=True)
  name = models.CharField(max_length=200)
  quantity = models.IntegerField(default=1)
  notes = models.TextField(blank=True)
  stripe_product_identifier = models.CharField(max_length=107,blank=True)
  custom_fields = models.JSONField(blank=True,default=dict)
  json = models.JSONField(blank=True,default=dict)
  last_modified_date_time = models.DateTimeField(auto_now=True)

  image_2 = models.ImageField(null=True,blank=True)
  image_1 = models.ImageField(null=True,blank=True)
  image_3 = models.ImageField(null=True,blank=True)
  image_4 = models.ImageField(null=True,blank=True)
  image_5 = models.ImageField(null=True,blank=True)
  image_6 = models.ImageField(null=True,blank=True)
  image_7 = models.ImageField(null=True,blank=True)
  image_8 = models.ImageField(null=True,blank=True)
  image_9 = models.ImageField(null=True,blank=True)
  image_10 = models.ImageField(null=True,blank=True)

  category = models.JSONField(blank=True,default=dict)

  size = models.JSONField(blank=True,default=dict)
  
  upc = models.IntegerField(null=True,blank=True)

  unit_of_measurement_length = models.CharField(max_length=200,blank=True,choices=uom_len_choices)
  package_length = models.CharField(max_length=200,null=True,blank=True)
  package_width = models.CharField(max_length=200,null=True,blank=True)
  package_depth = models.CharField(max_length=200,null=True,blank=True)

  unit_of_measurement_mass = models.CharField(max_length=200,blank=True,choices=uom_mass_choices)
  package_weight = models.CharField(max_length=200,null=True,blank=True)

  price = models.ManyToManyField("products.price",related_name="+")
  stripe_price_identifier = models.CharField(max_length=107,blank=True)

  def __str__(self) -> str:
    if self.sku == "":
      return f'{self.name}'
    else:
      return f'{self.sku} | {self.name}'

  # sold_to_contact = models.ForeignKey('crm.contact',on_delete=models.CASCADE,null=True,blank=True)
  

  def update(self,**kwargs):

    for kw, value in kwargs.items():

      # if product model has attribute
      # update model & save
      if hasattr(Product,kw):
        setattr(self,kw,value)
      self.save()

      # if keyword passed in list update Stripe product
      if kw == "active":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          active = value,
        )
      elif kw == "description":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          description = value,
        )
      elif kw == "metadata":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          matadata = value,
        )
      elif kw == "name":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          name = value,
        )
      elif kw == "images":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          images = value,
        )
      elif kw == "package_dimensions":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          package_dimensions = value,
        )
      elif kw == "shippable":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          shippable = value,
        )
      elif kw == "statement_descriptor":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          statement_descriptor = value,
        )
      elif kw == "tax_code":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          tax_code = value,
        )
      elif kw == "unit_label":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          unit_label = value,
        )
      elif kw == "url":
        stripe.Product.modify(
          sid=self.stripe_product_identifier,
          url = value,
        )



@receiver(pre_save, sender=Product)
def create_stripe_product(sender, instance, **kwargs):
  stripe.api_key = settings.STRIPE_SECRET_KEY
  if instance.sku != '' and instance.name != '' and instance.stripe_product_identifier == '':


    name = str(instance.sku) + " " + str(instance.name)

    if instance.notes != '':
      product = stripe.Product.create(
        name=name,
        description=instance.notes,
      )
    else:
      product = stripe.Product.create(
        name=name,
      )
    instance.stripe_product_identifier = product.id

  if instance.price == None and instance.stripe_price_identifier != '':
    # Convert decimal string to integer amount
    string_amount = str(instance.price)
    replaced_string_amount = string_amount.replace(".","")
    int_amount = int(replaced_string_amount)   
    
    # Create price
    price = stripe.Price.create(
      unit_amount=int_amount,
      currency="usd",
      product=instance.stripe_product_identifier,
    )
    instance.stripe_price_identifier = price.id