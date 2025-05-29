from django.http import HttpRequest
from django.shortcuts import render
from .models import ArticleModel
# Create your views here.
from django.views import View


class ArticleView(View):
    def get(self, request:HttpRequest):
        articels = ArticleModel.objects.all()
        return render(request, 'article_page.html', {
            'articels' : articels

        })
class ArticleDetailView(View):
    def get(self, request, slug):
        article = ArticleModel.objects.filter(slug=slug).first()
        return render(request, 'details_article.html', {
            'article' : article

        })
