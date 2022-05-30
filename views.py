from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Django!')

def v1(response):
    return HttpResponse('View 1!')
     

# Create your views here.
