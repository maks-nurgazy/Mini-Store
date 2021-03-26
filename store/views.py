from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from store.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'


class ProductListView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired
    template_name = 'products/product-list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
