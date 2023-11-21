from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pushpa(request):
    return render(request,'pushpa.html')

def arya(request):
    return HttpResponse('<h1>Arya is Allu Aruns film</h1>')
