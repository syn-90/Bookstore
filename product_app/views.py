from django.shortcuts import render, redirect
from .models import ProductModel, AuthorModel, CategoryModel
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = 'product_list.html'
    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()
        return context

class ProductDetailsView(View):
    def get(self, request, slug):
        product = ProductModel.objects.filter(slug=slug).first()
        if product is not None:
            return render(request, 'products_details.html',{
                'product':product
            })

        else :
            redirect('home_page')

class CategoryView(View):
    def get(self, request, slug):
        products = ProductModel.objects.filter(category__slug=slug)
        if products is not None:
            return render(request, 'product_list.html',{
                'products':products
            })

        else :
            redirect('home_page')