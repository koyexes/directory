from django import forms
from django.core.exceptions import ObjectDoesNotExist

from.models import Paylater_Debtor

class Search(forms.Form):
    search = forms.CharField(widget = forms.TextInput(attrs = {'id' : 'searchField','required' : 'True',                                                             'class' :
        'form-control'}))


    def find(self):
        data = self.cleaned_data
        try:
            query_set = Paylater_Debtor.objects.filter(AccountHolderName__icontains = data['search'])
        except ObjectDoesNotExist:
            query_set = 'No Record Found'

        return query_set