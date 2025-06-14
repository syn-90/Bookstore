from django.contrib import admin
from django.urls import path, include
from.views import *

urlpatterns = [
    path('', ProductView.as_view(), name = 'product_list'),
    path('details/<slug>/', ProductDetailsView.as_view(), name = 'products_details'),
    path('category/<slug>/', CategoryView.as_view(), name = 'category_page'),
    path('author/<slug>/', AuthorsView.as_view(), name = 'authors_page')
]



