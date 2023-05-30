from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexMain.as_view(), name='main'),
    path('tools', IndexTools.as_view(), name='tools'),
    path('orders', IndexOrderStore.as_view(), name='orders'),
    path('deliveries', IndexDeliveryStore.as_view(), name='deliveries'),
    path('m_deliveries', IndexManualDeliveryStore.as_view(), name='m_deliveries'),
    path('products', IndexProduct.as_view(), name='products'),
]