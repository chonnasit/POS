# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Owners(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    ID_card = models.CharField(max_length=13)
    ID_job = models.CharField(max_length=5)
    store_name = models.CharField(max_length=200)


class Table(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    number = models.CharField(max_length=3)
    Quantity = models.CharField(max_length=5)
    Order_id = models.TextField(max_length=255)
    status_table = models.CharField(max_length=255)


class Q(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Order_id = models.TextField(max_length=255)


class Employee(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    User = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    jobposition = models.CharField(max_length=255)
    ID_card = models.CharField(max_length=50)
    ID_job = models.CharField(max_length=50)
    ID_bank = models.CharField(max_length=50)
    Bank = models.CharField(max_length=255)
    Salary = models.IntegerField()


class category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    category = models.CharField(max_length=255)


class Menu(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    category = models.CharField(max_length=255)
    foodname = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    status_menu = models.CharField(max_length=5)


class Order(models.Model):
    Order_id = models.AutoField(auto_created=True, primary_key=True)
    type_order = models.TextField(max_length=255)
    number_table = models.TextField(max_length=255)
    name = models.TextField(max_length=255)
    status_order = models.TextField(max_length=100)
    total = models.TextField(max_length=255)


class Orderlish(models.Model):
    Orderlish_id = models.AutoField(auto_created=True, primary_key=True)
    Order_id = models.ForeignKey('Order', db_column='Order_id', blank=True)
    nume_food = models.TextField(max_length=255)
    price = models.IntegerField()
    total_price = models.IntegerField()
    category = models.TextField(max_length=255)
    status = models.TextField(max_length=255)


class receipt(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True)
    Order_id = models.ForeignKey('Order', db_column='Order_id', blank=True)


class Tip(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True)
    Order_id = models.ForeignKey('Order', db_column='Order_id', blank=True)
    time_day = models.CharField(max_length=255)
    tip_cash = models.IntegerField()
    tip_tran = models.IntegerField()
    tip_total = models.IntegerField()


class Bill_Setting(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True)
    StoreName = models.TextField()
    VAT = models.IntegerField()
    SC = models.IntegerField()
    EndTextBill = models.TextField()
