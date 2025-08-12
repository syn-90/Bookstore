from django.contrib import admin
from django.urls import path, include
from.views import *




urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register_page'),
    path('otp-code/<id>/',OtpView.as_view(), name = 'otp_page'),
    path('login/', Login.as_view(), name = "login_page"),
    path('logout/', Logout.as_view(), name = 'logout')
]