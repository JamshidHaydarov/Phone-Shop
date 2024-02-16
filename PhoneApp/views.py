from django.shortcuts import render
from .models import Phone

def mainmenu(request):
    return render(request, 'base.html', context={})

def contents(request):
    phones = Phone.objects.all()
    return render(request, 'phone-list.html', context={'phones': phones})

# Create your views here.
