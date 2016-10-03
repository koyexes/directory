from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import Search
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    if request.method == 'POST':
        return render(request, 'debtors/index.html', {})
        return HttpResponseRedirect('https://www.google.com')

    else:
        search_form = Search(auto_id = False)
        context = {'search_form' : search_form}
        return render(request,  'debtors/index.html', context)


def search(request):
    return HttpResponseRedirect('https://www.google.com')