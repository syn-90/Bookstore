from django.shortcuts import render
from django.views import View
from .models import ArticleModel
# Create your views here.


class ArticelsPage(View):
    def get(self,request):
        articels = ArticleModel.objects.filter(is_active=True)
        return render(request, 'article_page.html',{
            'articels' : articels

        })


class DetailView(View):
    def get(self, request, slug):
        article = ArticleModel.objects.filter(slug=slug).first()
        return render(request, 'article_details.html', {
            'article' : article
        })