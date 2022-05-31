from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Address(models.Model):

    street_1 = models.CharField(max_length=200)
    street_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=11)
    contact = models.ManyToManyField('contacts.Contact')