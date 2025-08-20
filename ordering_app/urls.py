from django.contrib import admin
from django.urls import path, include
from.views import *





urlpatterns = [
    path("", OrderView.as_view() , name = 'order_page'),
    path('add_order/' , add_to_order),
    path('change_count/' , change_count_basket),
    path('remove_detail/', remove_detail)
]