from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    
class Ninja(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dojo = models.ForeignKey(Dojos, null=True,related_name="codingdojo", on_delete=models.PROTECT)