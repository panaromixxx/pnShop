from django.shortcuts import render
from .models import Product, Order

# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'shop': products})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'shop/orders.html', {'orders': orders})

def product_detail(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'shop/productdetail.html', {'products': products})