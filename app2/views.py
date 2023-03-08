from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kholi(request):
    return HttpResponse('<h1>kholi is best batsman</h1>')
def abd(request):
    return HttpResponse('<h1>abd is mr360</h1>')