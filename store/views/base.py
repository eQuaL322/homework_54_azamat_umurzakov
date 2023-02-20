from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from store.models import Product, Category


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_view.html', context=context)


def product_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={
        'product': products,
    })
