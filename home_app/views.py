from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home_page.html'




def header_component(request):
    return render(request, 'header.html', {

    })


def footer_component(request):
    return render(request, 'footer.html', {

    })