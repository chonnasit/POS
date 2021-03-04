# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Owner(models.Model):
    email = models.charFileld(max_length=255)
    password = models.charFileld(max_length=255)
