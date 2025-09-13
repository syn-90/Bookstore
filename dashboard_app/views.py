from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import FavoriteProductsModel
# Create your views here.
from ordering_app.models import BasketOrderModel
from utils.check_pattern import CheckPattern
# @method_decorator(login_required, name='dispatch')
from user_app.models import UserModel


class DashboardView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'dashboard_page.html', {
                'user' : user

            })
    def post(self, request):
        user = request.user
        user_name = request.POST.get('user_name')
        new_avatar = request.FILES.get('new_avatar')

        if UserModel.objects.filter(username=user_name).exclude(id=user.id).exists():
            return render(request, 'dashboard_page.html', {
                'user': user,
                'name_error': True
            })
        else:
            user.username = user_name
            if new_avatar:   # اگر کاربر عکس جدید انتخاب کرده باشه
                user.avatar = new_avatar
                change_avatar = True
            user.save()
            if change_avatar:
                return render(request, 'dashboard_page.html', {
                    'user': user,
                    'change_avatar': True
                })
            else:
                return render(request, 'dashboard_page.html', {
                    'user': user,
                    'change_name': True
                })



class ChangePasswordView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'change_password_page.html', {


            })
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            password = request.POST.get('password')
            if user.check_password(password):
                new_password = request.POST.get('new_password')
                confirm_new_password = request.POST.get('confirm_new_password')
                password_valid = CheckPattern(new_password)
                if password_valid.check_password_letter_number():
                    if new_password == confirm_new_password :
                        user.set_password(new_password)
                        user.save()
                        return render(request, 'change_password_page.html', {
                            'change_password': True

                        })
                    else:
                        return render(request, 'change_password_page.html', {
                            'confirm_error' : True

                        })
                else:
                    return render(request, 'change_password_page.html', {
                        'not_valid_password' : True
                    })
            else:
                return render(request, 'change_password_page.html', {
                    'passwod_error' : True
                })



class OrderDashboardView(View) :
    def get(self, requset):
        user = requset.user
        baskets = BasketOrderModel.objects.prefetch_related('orderdetailmodel_set__product').filter(user_id=user.id)

        return render(requset, "order_page_dashboard.html", {
            'user' : user,
            'baskets' : baskets
        })

class FavoriteProductsView(View):
    def get(self, request):
        user = request.user
        favorites = FavoriteProductsModel.objects.filter(user_id=user.id)
        return render(request, 'favorite_page.html', {
            'favorites' : favorites

        })

# def add_to_favorite(request):
#     if request.user.is_authenticated:
#         user = request.user
#         product_id = int(request.GET.get('product_id'))
#         favorite_product = FavoriteProductsModel.objects.filter(product_id=product_id, user_id=user.id).first()
#         if favorite_product is not None:
#             return JsonResponse({'status': 'already_add'})
#         else:
#             favorite_product = FavoriteProductsModel(product_id=product_id, user_id=user.id)
#             favorite_product.save()
#             return JsonResponse({'status' : 'success'})
#     else:
#         return JsonResponse({'status': 'not_login'})


# views.py


def add_to_favorite(request):
    if request.method == 'GET' :
         if request.user.is_authenticated:
            product_id = request.GET.get('product_id')

            favorite, created = FavoriteProductsModel.objects.get_or_create(user=request.user,product_id=product_id)

            if created:
                return JsonResponse({'status': 'success'})
            else:
                favorite.delete()
                return JsonResponse({'status': 'already_add'})
         else:
            return JsonResponse({'status': 'not_login'})