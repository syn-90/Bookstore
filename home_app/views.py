from django.shortcuts import render
from django.views.generic import TemplateView
from product_app.models import CategoryModel


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_page.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data( **kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context


def header_component(request):
    return render(request, 'header.html', {

    })


def footer_component(request):
    return render(request, 'footer.html', {

    })
