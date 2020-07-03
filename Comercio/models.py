from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length = 30)
    ciudad = models.CharField(max_length = 30)
