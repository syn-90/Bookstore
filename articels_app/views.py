from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import ArticleModel, ArticleCommentModel
# Create your views here.


class ArticelsPage(View):
    def get(self,request):
        articels = ArticleModel.objects.filter(is_active=True)
        return render(request, 'article_page.html',{
            'articels' : articels

        })


class DetailView(View):
    def get_article(self, slug):
        article = ArticleModel.objects.prefetch_related('articlecommentmodel_set').filter(slug=slug).first()
        if article is not None:
            return article
        else:raise Http404

    def get(self, request, slug):
        article = self.get_article(slug)
        return render(request, 'article_details.html', {
            'article' : article
        })
    def post(self, request, slug):
        article = self.get_article(slug=slug)
        user = request.user
        text = request.POST.get('message')
        if len(text.strip()) > 3 :
            # if request.user.is_athenticated():

                new_comment = ArticleCommentModel(user=user, article=article, text=text, is_publish=False)
                new_comment.save()
                print('ok')
                return render(request, 'article_details.html', {
                    'article' : article ,
                    'status' : 'seccess'
                })
            # else:
            #     return render(request, 'article_details.html', {
            #         'article': article,
            #         'login_error': 'True'
            #     })

        else :
            return render(request, 'article_details.html', {
                'article' : article ,
                'message_error' : True
            })



