import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s. </h3></body></html>" % now
    return HttpResponse(html)

def password(request):
    return render(request, 'web_interface/password.html')

def neuro(request):
    return render(request, 'web_interface/neuro-interface.html')

def shablon(request):
    return render(request, 'web_interface/model.html')

def graphs(request):
    return render(request, 'web_interface/graphs.html')

def test(request):
    return render(request, 'web_interface/test.html')

