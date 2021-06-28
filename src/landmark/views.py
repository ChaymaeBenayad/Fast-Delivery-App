from django.shortcuts import render

from account.models import Account

# Create your views here.

def home_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
  
    return render(request, "landmark/home.html", context)