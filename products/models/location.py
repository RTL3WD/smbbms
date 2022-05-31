from django.db import models

# Create your models here.

class Location(models.Model):
  
  alias = models.CharField(max_length=200)
  street_1 = models.CharField(max_length=200)
  street_2 = models.CharField(max_length=200,blank=True)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zip_code = models.CharField(max_length=11)

  def __str__(self) -> str:
      return f'{self.alias}'