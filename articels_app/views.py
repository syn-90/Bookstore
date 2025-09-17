from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import ArticleModel, ArticleCommentModel
# Create your views here.


class ArticelsPage(View):
    def get(self,request):
        articels = ArticleModel.objects.filter(is_active=True)
        paginator = Paginator(articels, 3)
        page_number = request.GET.get('page')
        try:
            articels = paginator.page(page_number)
        except PageNotAnInteger:
            articels = paginator.page(1)
        except EmptyPage:
            articels = paginator.page(paginator.num_pages)
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



def send_comment(request):
    try:
        print('hi')
        article_id = request.GET.get('article_id')
        text = request.GET.get('text')
        new_comment = ArticleCommentModel(article_id=article_id,user_id=request.user.id , text=text )
        new_comment.save()
        return JsonResponse({'status': 'success'})
    except Exception as err:
        return JsonResponse({'status': 'field'})

