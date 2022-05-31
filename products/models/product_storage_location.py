from django.db import models

from .product import Product
from .storage_location import StorageLocation

# Create your models here.

class ProductStorageLocation(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} | {self.location}'