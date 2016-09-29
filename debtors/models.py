from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paylater_Debtors(models.Model):
    AccountHolderName  = models.CharField(max_length = 255)
    Employer = models.CharField(max_length = 255)
    TotalDue = models.BigIntegerField()
    Balance = models.BigIntegerField()
    DaysInArrears = models.IntegerField()
    MobilePhone = models.CharField(max_length = 15)





