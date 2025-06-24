from django.contrib import admin
from django.urls import path, include
from.views import *





urlpatterns = [
    path("", OrderView.as_view() , name = 'order_page')
]