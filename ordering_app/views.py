from django.shortcuts import render

# Create your views here.
from django.views import View


class OrderView(View):
    def get(self, request):
        return render(request, 'order_page.html', {

        })