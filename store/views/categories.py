from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from store.models import Category


def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_add.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    category = Category.objects.create(**category_data)

    return redirect(request, 'products_view.html')
