from django.urls import path

from store.views import category_list, product_detail

urlpatterns = [
    path('', category_list, name='product_list'),
    path('<slug:category_slug>', category_list, name='products_by_category'),
    path('<int:id>/', product_detail, name='product_detail'),
]
