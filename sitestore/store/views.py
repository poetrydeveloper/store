from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Привет мир</h1>')

def tools(request):
    return HttpResponse('<h1>tools</h1>')