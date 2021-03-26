from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from store.models import Product, Category


class HomeView(TemplateView):
    template_name = 'home.html'


def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/product-list.html', {
        'categories': categories,
        'category': category,
        'products': products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product-detail.html', {'product': product})
