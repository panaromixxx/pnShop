from django.urls import path, include
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('order/', orders, name='orders'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail')
]