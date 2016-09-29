from django.contrib import admin
from .models import Paylater_Debtors

# Register your models here.

class PaylaterDebtors(admin.ModelAdmin):
    list_display = ('AccountHolderName')


admin.site.register(Paylater_Debtors, PaylaterDebtors)
