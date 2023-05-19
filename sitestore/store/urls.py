from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('tools', IndexTools.as_view(), name='tools'),
    path('orders', IndexOrderStore.as_view(), name='orders'),
]