from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import ProductModel, AuthorModel, CategoryModel
from django.views import View
# Create your views here.



class ProductView(View):
    def get(self, request):
        products = ProductModel.objects.all()
        categories = CategoryModel.objects.all()
        paginator = Paginator(products,4)
        page_number = request.GET.get('page')
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, 'product_list.html', {
            'products': products ,
            'categories':categories
        })
# class ProductView(TemplateView):
#     template_name = 'product_list.html'
#     def get_context_data(self, **kwargs):
#         context = super(ProductView, self).get_context_data(**kwargs)
#         context["products"] = ProductModel.objects.all()
#         return context

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

class AuthorsView(View):
    def get(self, request, slug):
        author = AuthorModel.objects.filter(slug=slug).first()
        categories =CategoryModel.objects.filter(authormodel=author)

        if author is not None:
            return render(request, 'authors_page.html',{
                'author':author,
                'categories':categories
            })

        else :
            redirect('home_page')


