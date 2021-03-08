# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Owners(models.Model):
    id  = models.AutoField(auto_created=True,primary_key=True)
    firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    ID_card = models.CharField(max_length=13)
    ID_job= models.CharField(max_length=5)
    store_name= models.CharField(max_length=200)

class Table(models.Model):
    id  = models.AutoField(auto_created=True,primary_key=True)
    number = models.CharField(max_length=3)
    Quantity = models.CharField(max_length=2)
    time = models.CharField(max_length=10)
    Order_id = models.CharField(max_length=255)

class Employee(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    User = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    jobposition = models.CharField(max_length=255)
    ID_card  = models.CharField(max_length=255)
    ID_job = models.CharField(max_length=255)
    ID_bank = models.CharField(max_length=255)
    Bank = models.CharField(max_length=255)
    Salary = models.CharField(max_length=255)

class food(models.Model):
    id  = models.AutoField(auto_created=True,primary_key=True)
    category = models.CharField(max_length=255)
    foodname = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.IntegerField()
    image = models.CharField(max_length=255)

class Order(models.Model):
    Order_number = models.IntegerField()
    list = models.TextField(max_length=255)
    priceorder = models.IntegerField()
    number = models.IntegerField()
    price = models.IntegerField()
    type_food = models.TextField(max_length=255)
    List_ID = models.IntegerField()

class Orderlish(models.Model):
    #List_ID = models.AutoField(auto_created=True)
    types_order = models.TextField(max_length=255)
    number_order = models.TextField(max_length=255)
    number_table = models.TextField(max_length=255)
    status = models.TextField(max_length=3)

class receipt(models.Model):
	#id = models.IntegerField()
	order = models.TextField(max_length=255)
	number = models.IntegerField()
	time = models.IntegerField()
	manager = models.TextField(max_length=255)
