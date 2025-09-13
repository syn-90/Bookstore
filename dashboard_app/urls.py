from django.contrib import admin
from ordering_app.views import remove_detail
from .views import *
from django.urls import path


urlpatterns = [
   path('', DashboardView.as_view(), name='dashboard_page'),
   path('change_password/',ChangePasswordView.as_view(), name='change_password' ),
   path('order/' , OrderDashboardView.as_view() , name = 'order_page_dashboard'),
   path('add_to_favorite/' , add_to_favorite) ,
   path('favorite/', FavoriteProductsView.as_view(), name = 'favorite_page'),
   path('favorite/remove_detail/', remove_detail)
]