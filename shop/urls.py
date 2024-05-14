from django.urls import path, include
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('order/', orders, name='orders'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('createorder/<int:product_id>/', create_order, name='create_order'),
]