from django.urls import path

from store.views.base import products_view, product_view

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/<int:pk>', product_view, name='product_view')
]
