from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Search
from django.core.urlresolvers import reverse




# Create your views here.

def index(request):

        search_form = Search(auto_id = False)
        result = search_form.populate(3)
        context = {'search_form' : search_form, 'result' : result, 'no_result_flag' : False}
        return render(request,  'debtors/index.html', context)

def search(request):
    if request.method == 'GET':
        if request.GET.get('search'):
            search_form = Search(request.GET)
            if search_form.is_valid():
                data = search_form.find(3 )
                result = data[0]
                no_result_flag = data[1]
                if no_result_flag:
                    result = 'No Record Found'
                context = {'search_form': search_form, 'result' : result, 'no_result_flag' : no_result_flag}
                return render(request, 'debtors/index.html', context)
        else:
            return HttpResponseRedirect(reverse('debtors:index'))






