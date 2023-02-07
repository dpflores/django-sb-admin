# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# class DataKomatsu(models.Model):
#     id = models.AutoField(primary_key=True)
#     serie = models.CharField(max_length=255)
#     temperature = models.FloatField()
#     current = models.FloatField()
#     voltage = models.FloatField()
#     status = models.CharField(max_length=255)
#     horometer = models.FloatField()


class Accelerations(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    serie = models.CharField(max_length=60)
    accelx = models.FloatField()
    accely = models.FloatField()
    accelz = models.FloatField()

    class Meta:
        managed = False
        db_table = 'accelerations'


class FurnanceData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    temperature = models.FloatField()
    current = models.FloatField()
    voltage = models.FloatField()
    status = models.CharField(max_length=50)
    horometer = models.FloatField()
    serie = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'furnance_data'