"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from Config import settings
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('products/', include('product_app.urls')),
    path('contact_us/', include('contact_app.urls')),
    path('users/', include('user_app.urls')),
    path('articels/', include('articels_app.urls')),
    path('order/', include('ordering_app.urls')),

]


urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
