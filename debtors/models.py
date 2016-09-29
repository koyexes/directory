from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paylater_Debtor(models.Model):
    AccountHolderName  = models.CharField(max_length = 255, verbose_name = 'Account Holder')
    Employer = models.CharField(max_length = 255, blank = True)
    TotalDue = models.BigIntegerField()
    Balance = models.BigIntegerField()
    DaysInArrears = models.IntegerField()
    MobilePhone = models.CharField(max_length = 15, blank = True)





