from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from ordering_app.models import BasketOrderModel

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
        new_avatar = request.FILES.get('new_avatar')  # تغییر مهم اینجاست 👈

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


class OrderDashboardView(View) :
    def get(self, requset):
        user = requset.user
        baskets = BasketOrderModel.objects.prefetch_related('orderdetailmodel_set__product').filter(user_id=user.id)

        return render(requset, "order_page_dashboard.html", {
            'user' : user,
            'baskets' : baskets
        })

