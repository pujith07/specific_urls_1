from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<marquee>Dhoni is best finisher</marquee>')
def raina(request):
    return HttpResponse('<h1>Raina is MR IPL</h1>')