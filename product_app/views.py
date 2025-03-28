from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = 'product_list.html'