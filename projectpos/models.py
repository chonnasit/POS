# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Owner(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    ID_card = models.CharField(max_length=13)
    ID_job= models.CharField(max_length=5)
    store_name= models.CharField(max_length=200)

class Table(models.Model):
    number = models.CharField(max_length=3)
    people = models.CharField(max_length=2)
    time = models.CharField(max_length=10)
    order = models.CharField(max_length=255)
