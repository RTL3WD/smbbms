from django.conf import settings
from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image_1', 'get_products']

class Image(models.Model):

    products = models.ManyToManyField("products.Product")
    image_1 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_2 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_3 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_4 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_5 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_6 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_7 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_8 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_9 = models.ImageField(null=True,blank=True, upload_to="images/")
    image_10 = models.ImageField(null=True,blank=True, upload_to="images/")

    def get_products(self):
        products = list(self.products.all())
        products_str = ""

        for product in products:
            sku = product.sku
            name = product.name
        
            if product == products[-1] or len(products) == 1:
                products_str = products_str + f"( { sku } | { name } )"
            else:
                products_str = products_str + f"( { sku } | { name } ) , "

        return f"{products_str}"