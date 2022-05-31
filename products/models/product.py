from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import json, stripe

# TODO:
# 
# FIXME:
# 

# Create your models here.

class Product(models.Model):

  size_choices = (
    ('xxxs','XXX-Small'),
    ('xxs','XX-Small'),
    ('xs','X-Small'),
    ('s','Small'),
    ('m','Medium'),
    ('lg','Large'),
    ('xlg','X-Large'),
    ('xxlg','XX-Large'),
    ('xxxlg','XXX-Large'),
  )

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

  name = models.CharField(max_length=200)
  sku = models.CharField(max_length=200,blank=True)
  quantity = models.IntegerField(default=1)
  notes = models.TextField(blank=True)
  
  stripe_product_identifier = models.CharField(max_length=107,blank=True)

  custom_fields = models.JSONField(blank=True,default=dict)

  created_date_time = models.DateTimeField(auto_now_add=True)
  last_modified_date_time = models.DateTimeField(auto_now=True)

  category = models.JSONField(blank=True,default=dict)
  size = models.CharField(blank=True,choices=size_choices,max_length=200) 
  upc = models.IntegerField(null=True,blank=True)

  unit_of_measurement_length = models.CharField(max_length=200,blank=True,choices=uom_len_choices)
  package_length = models.CharField(max_length=200,null=True,blank=True)
  package_width = models.CharField(max_length=200,null=True,blank=True)
  package_depth = models.CharField(max_length=200,null=True,blank=True)

  unit_of_measurement_mass = models.CharField(max_length=200,blank=True,choices=uom_mass_choices)
  package_weight = models.CharField(max_length=200,null=True,blank=True)

  class Meta:
    indexes = [models.Index(fields=['sku', 'name', ]),]

  def __str__(self) -> str:
    if self.sku == "":
      return f'{self.name}'
    else:
      return f'{self.sku} | {self.name}'

  def returnjson(self):

    name = str(self.name)
    sku = str(self.sku)
    quantity = str(self.quantity)
    notes = str(self.notes)
    
    stripe_product_identifier = str(self.stripe_product_identifier)

    custom_fields = str(self.custom_fields)

    created_date_time = str(self.created_date_time)
    last_modified_date_time = str(self.last_modified_date_time)

    category = str(self.category)
    size = str(self.size)
    upc = str(self.size)
    unit_of_measurement_length = str(self.unit_of_measurement_length)
    package_length = str(self.package_length)
    package_width = str(self.package_width)
    package_depth = str(self.package_depth)

    unit_of_measurement_mass = str(self.unit_of_measurement_mass)
    package_weight = str(self.package_weight)

    data = {
      "name": name,
      "sku": sku,
      "quantity": quantity,
      "notes": notes,
      "stripe product identifier": stripe_product_identifier,
      "custom fields": custom_fields,
      "category": category,
      "size": size,
      "upc": upc,
      "unit of measurement length": unit_of_measurement_length,
      "package length": package_length,
      "package width": package_width,
      "package depth": package_depth,
      "unit of measurement mass": unit_of_measurement_mass,
      "package_weight": package_weight,
    }

    # Convert dict to string
    data_string = json.dumps(data)
      
    # Converting string to json
    final_json = json.loads(data_string)
    return final_json

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