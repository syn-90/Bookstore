from django.contrib import admin
from django.urls import path, include
from.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register_page')
]