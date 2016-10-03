from django import forms

class Search(forms.Form):
    search = forms.CharField(widget = forms.TextInput(attrs = {'id' : 'searchField', 'required' : 'True', 'class' :
        'form-control'}))