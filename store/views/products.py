from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from store.models import Category, Product


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'product_add.html', context=context)

    category_id = request.POST.get('category')
    category = Category.objects.get(id=category_id)
    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category': category,
        'price': request.POST.get('price'),
        'image': request.POST.get('image')
    }
    product = Product.objects.create(**product_data)

    return redirect(reverse('product_view', kwargs={'pk': product.pk}))


def product_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={
        'product': products,
    })
