from django.shortcuts import render
from .forms import Search




# Create your views here.

def index(request):

        search_form = Search(auto_id = False)
        context = {'search_form' : search_form}
        return render(request,  'debtors/index.html', context)

def search(request):
    if request.method == 'GET':
        if request.GET.get('search'):
            search_form = Search(request.GET)
            if search_form.is_valid():
                result = search_form.find()
                flag = False
                if not result:
                    result = 'No Record Available'
                    flag = True
                context = {'search_form': search_form, 'result' : result, 'flag' : flag}
                return render(request, 'debtors/index.html', context)






