from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from store.models import Product


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_view.html', context=context)
