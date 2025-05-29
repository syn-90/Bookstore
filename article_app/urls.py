from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleView.as_view(), name = 'article_page'),
    path('details/<slug>/', ArticleDetailView.as_view(), name= 'details_article')

]