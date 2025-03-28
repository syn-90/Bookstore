from django.contrib import admin
from django.urls import path, include
from.views import *

urlpatterns = [
    path('', ProductView.as_view(), name = 'product_list')
]