from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import pre_save
from django.dispatch import receiver

import stripe

from .contact import Contact

# Create your models here.

class BusinessAdmin(admin.ModelAdmin):
    # list_filter = ['name']
    list_display = ['id','business_name']
    search_fields = ['id','business_name']

class Business(models.Model):

    business_type_choices = (
        ('sole_proprietorship','Sole Proprietorship'),
        ('partnership','Partnership'),
        ('corporation','Corporation'),
        ('s-corporation','S-Corporation'),
        ('limited_liability_company','Limited Liability Company (LLC)'),
    )
        
    # Primary Fields
      
    # Contact Type
    business_type = models.CharField(max_length=200,choices=business_type_choices)
    
    # Business Information
    # Business Name optional
    business_name = models.CharField(max_length=200,blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    business_tax_id = models.CharField(max_length=200,blank=True)

    # Contact's phone
    business_phone = models.CharField(max_length=15,blank=True)
    # Contact's email
    business_email = models.EmailField(blank=True)

    # Contact's Business Address
    business_street_address_1 = models.CharField(max_length=200,blank=True)
    business_street_address_2 = models.CharField(max_length=200,blank=True)
    business_city = models.CharField(max_length=200,blank=True)
    business_state = models.CharField(max_length=200,blank=True)
    business_zip_code = models.CharField(max_length=200,blank=True)

    # List of associated parties

    # Methods
    def __str__(self):
        return f'{self.business_name}'