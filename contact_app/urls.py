from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns =[
    path('',ContactView.as_view(), name = 'contact_page' )
]