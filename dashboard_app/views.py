from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


# @method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'dashboard_page.html', {
                'user' : user

            })

class ChangePasswordView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'change_password_page.html', {


            })

