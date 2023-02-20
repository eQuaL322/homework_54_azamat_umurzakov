from django.contrib import admin

from store.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'image', 'created_date')
    list_filter = ('id', 'title', 'category', 'price', 'created_date')
    search_fields = ('title', 'description', 'category')
    fields = ('title', 'description', 'category', 'price', 'image')


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    search_fields = ('title', 'description')
    fields = ('title', 'description')


admin.site.register(Category, CategoryAdmin)
