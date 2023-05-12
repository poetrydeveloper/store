from django.shortcuts import render
from django.http import HttpResponse
from .models import Tools

def index(request):
    return HttpResponse('<h1>Привет мир</h1>')

def indexTools(request):
    tools = Tools.objects.all()
    context = {
        'tools': tools,
        'title': 'Список инструментов'
    }
    return render(request, 'tools/indexTools.html', context)