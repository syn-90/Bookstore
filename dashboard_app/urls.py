from django.contrib import admin
from .views import *
from django.urls import path


urlpatterns = [
   path('', DashboardView.as_view(), name='dashboard_page'),
   path('change_password',ChangePasswordView.as_view(), name='change_password' )
]