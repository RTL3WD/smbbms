from django.db import models

from .location import Location

# Create your models here.

class StorageLocation(models.Model):

  stock_location_choices = (
    ('physical','Physical'),
    ('virtual','Virtual'),
  )

  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100, choices=stock_location_choices, default='physical')
  location = models.ForeignKey(Location, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return f'{self.name} | {self.location} | {self.type}'