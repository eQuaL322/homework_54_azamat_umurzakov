from django.urls import path

from store.views.base import products_view
from store.views.categories import category_add_view
from store.views.products import product_add_view, product_view

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products', products_view, name='products_view'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/add', product_add_view, name='product_add_view')
]
