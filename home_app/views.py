from django.shortcuts import render
from django.views.generic import TemplateView
from product_app.models import CategoryModel, ProductModel
from ordering_app.models import BasketOrderModel


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_page.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data( **kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['new_products'] = ProductModel.objects.order_by('-id')[:3]
        context['off_products'] = ProductModel.objects.filter(is_off__isnull = False )[:4]
        return context


def header_component(request):
    user = request.user
    if user.is_authenticated :
        basket = BasketOrderModel.objects.prefetch_related("orderdetailmodel_set").filter(user=user, is_paid=False).first()
        return render(request, 'header.html', {
            'basket' : basket

        })
    else:
        return render(request, 'header.html', {


        })



def footer_component(request):
    return render(request, 'footer.html', {

    })
