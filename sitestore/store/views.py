from django.shortcuts import render
from django.http import HttpResponse
from .models import Tools, OrderStore

from django.views.generic import ListView

def index(request):
    return HttpResponse('<h1>Привет мир</h1>')


class IndexTools(ListView):
    model = Tools
    template_name = 'tools/indexTools.html'
    context_object_name = 'tools'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список инструментов'
        return context

def indexOrderStore(request):
    # students = python.student_set.all()
    orders = OrderStore.objects.all()
    context = {
        'orders': orders,
        'title': 'Список заявок'
    }
    return render(request, 'orders/indexOrderStore.html', context)