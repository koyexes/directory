from django import forms
from django.core.exceptions import ObjectDoesNotExist

from.models import Paylater_Debtor

class Search(forms.Form):
    search = forms.CharField(widget = forms.TextInput(attrs = {'id' : 'searchField','required' : 'True',                                                             'class' :
        'form-control'}))


    def find(self, param = 3):
        data = self.cleaned_data
        try:
            query_set = Paylater_Debtor.objects.filter(AccountHolderName__icontains = data['search']).order_by('AccountHolderName')
            count = Paylater_Debtor.objects.filter(AccountHolderName__icontains = data['search']).count()
            if count < param:
                count = param
            result = [query_set[x:x + (count//param)] for x in xrange(0, count, count//param)]

        except ObjectDoesNotExist:
            result = 'No Record Found'

        return result

    def populate(self, param = 3):
        try:
            query_set = Paylater_Debtor.objects.all()
            count = Paylater_Debtor.objects.all().count()
            if count < param:
                count = param
            result = [query_set[x:x + (count//param)] for x in xrange(0, count, count//param)]
        except ObjectDoesNotExist:
            result = 'No Record Found'

        return result