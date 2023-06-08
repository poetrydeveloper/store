from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.views.generic import ListView


class IndexMain(ListView):
    model = MainPage
    template_name = 'main/main.html'
    context_object_name = 'main'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class IndexTools(ListView):
    model = Tools
    template_name = 'tools/indexTools.html'
    context_object_name = 'tools'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список инструментов'
        return context
    
class IndexOrderStore(ListView):
    model = OrderStore
    template_name = 'orders/indexOrderStore.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заявок'
        return context
    

class IndexDeliveryStore(ListView):
    model = DeliveryStore
    template_name = 'deliveries/indexDeliveryStore.html'
    context_object_name = 'deliveries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список Прихода товара'
        return context


class IndexManualDeliveryStore(ListView):
    model = ManualDeliveryStore
    template_name = 'deliveries/indexDeliveryStore.html'
    context_object_name = 'm_deliveries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ручной Список Прихода товара'
        return context

class IndexProduct(ListView):
    model = Product
    template_name = 'products/indexProduct.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        return context
    
class IndexProductCollections(ListView):
    model = CollectionProducts
    template_name = 'p_collections/indexProductCollection.html'
    context_object_name = 'p_collections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список сформированных товаров'
        return context
    
class IndexSales(ListView):
    model = Sales
    template_name = 'sales/indexSales.html'
    context_object_name = 'sales'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список продаж'
        return context