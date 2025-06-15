from django.contrib import admin
from django.urls import path, include
from.views import *

urlpatterns = [
    path('', ArticelsPage.as_view(), name = 'article_page'),
    path('details/<slug>/',DetailView.as_view(), name = 'article_details')
]