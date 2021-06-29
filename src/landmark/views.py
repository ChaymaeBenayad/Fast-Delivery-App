from django.shortcuts import render

from account.models import Account

# Create your views here.

def home_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
  
    return render(request, "landmark/home.html", context)

def location_view(request):
    return render(request, "landmark/MyLocation.html")

def Contact_view(request):
    return render(request, "landmark/ContactUs.html")

def optimalPath_view(request):
    return render(request, "landmark/optimalPath.html")    