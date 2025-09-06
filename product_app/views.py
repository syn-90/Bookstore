from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import ProductModel, AuthorModel, CategoryModel
from django.views import View
# Create your views here.



class ProductView(View):
    categories = CategoryModel.objects.all()
    authors = AuthorModel.objects.all()
    products = ProductModel.objects.all()

    def get(self, request):
        products = ProductView.products
        categories = ProductView.categories
        authors = ProductView.authors
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
            'categories':categories,
            'authors' : authors
        })
    def post(self, request):
        product_name = request.POST['product_name']
        product = ProductView.products.filter(title=product_name).first()
        print(product)
        categories = ProductView.categories
        authors = ProductView.authors
        if product is not None:
            return render(request, 'product_list.html', {
                'product': product,
                'categories': categories,
                'authors': authors
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
        try:
            products = ProductModel.objects.filter(category__slug=slug)
        except:
            products = ProductModel.objects.filter(author__slug=slug)
        categories = ProductView.categories
        if products is not None:
            return render(request, 'product_list.html',{
                'products':products ,
                'categories' : categories,
                'authors' : ProductView.authors
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

