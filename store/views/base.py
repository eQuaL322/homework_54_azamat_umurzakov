from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from store.models import Product, Category


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    category = get_object_or_404(Category)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products_view.html', context=context)


def product_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    category = get_object_or_404(Category)
    return render(request, 'product_view.html', context={
        'product': products,
        'category': category
    })
