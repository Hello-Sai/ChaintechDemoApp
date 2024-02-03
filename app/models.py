from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(unique=True,max_length=25,null=True,blank=True)
    email = models.EmailField(unique=True,max_length=25,null=True,blank=True)
    phone_number = models.CharField(max_length=25,null=True,blank=True)
    address = models.TextField()
