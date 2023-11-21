from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def gajini(request):
    return render(request,'gajini.html')

def brothers(request):
    return HttpResponse('<h1>Brothers is suryas film</h1>')