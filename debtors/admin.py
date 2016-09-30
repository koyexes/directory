from django.contrib import admin
from .models import Paylater_Debtor


# Register your models here.

class PaylaterDebtors(admin.ModelAdmin):
    list_display = ('AccountHolderName', 'Employer', 'TotalDue', 'Balance', 'DaysInArrears', 'MobilePhone')
    search_fields = ['AccountHolderName', 'Employer', 'TotalDue', 'Balance', 'DaysInArrears', 'MobilePhone']
    view_on_site = False


admin.site.register(Paylater_Debtor, PaylaterDebtors)
