from django.shortcuts import render

# Create your views here.
from django.views import generic

from products.models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'productes/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'productes/product_detail.html'
    context_object_name = 'products'