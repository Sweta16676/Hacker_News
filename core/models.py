from django.db import models

# Create your models here.
class CoreTable(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=20,unique=True)
    password = models.CharField(max_length=10)
