from django.shortcuts import render
from .models import ProductModel
# Create your views here.

from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = 'product_list.html'
    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()
        return context