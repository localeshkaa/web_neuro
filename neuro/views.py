from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'web_interface/home.html')

def password(request):
    return render(request, 'web_interface/password.html')

def neuro(request):
    return render(request, 'web_interface/neuro-interface.html')

def shablon(request):
    return render(request, 'web_interface/model.html')



