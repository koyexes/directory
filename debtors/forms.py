from django import forms
from django.core.exceptions import ObjectDoesNotExist

from.models import Paylater_Debtor

class Search(forms.Form):
    search = forms.CharField(widget = forms.TextInput(attrs = {'id' : 'searchField','class' : 'form-control'}))


    def find(self, param = 3):
        data = self.cleaned_data
        no_result_flag = False
        try:
            query_set = Paylater_Debtor.objects.filter(AccountHolderName__icontains = data['search']).order_by('AccountHolderName')
            count = Paylater_Debtor.objects.filter(AccountHolderName__icontains = data['search']).count()
            if count == 0:
                no_result_flag = True
                count = param
            elif count < param:
                count = param

            result = [query_set[x:x + (count//param)] for x in xrange(0, count, count//param)]

        except:
            result = ''

        return [result, no_result_flag]

    def populate(self, param = 3):
        try:
            query_set = Paylater_Debtor.objects.all()
            count = Paylater_Debtor.objects.all().count()
            if count < param:
                count = param
            result = [query_set[x:x + (count//param)] for x in xrange(0, count, count//param)]
        except:
            result = ''

        return result