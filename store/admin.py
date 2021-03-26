from django.contrib import admin

from store.forms import ProductForm
from store.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'get_category', 'price', 'image')

    def get_category(self, obj):
        return obj.category.first()

    get_category.short_description = 'Category'
    get_category.admin_order_field = 'name'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
