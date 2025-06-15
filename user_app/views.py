from django.contrib.auth import login, logout
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .models import UserModel
from .forms import RegisterForm, LoginForm
from utils.check_pattern import CheckPattern
from utils.utils import create_ranom_code
from services.email_sender_service import send_email


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_page.html', {
            'form': form

        })

    def post(self, request:HttpRequest):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("name")
                email = form.cleaned_data.get("email")
                phone_num = form.cleaned_data.get("phone_number")
                password = form.cleaned_data.get("password")
                confirm_password = form.cleaned_data.get("confirm_password")
                if UserModel.objects.filter(username=name).first() is not None:
                    return render(request, 'register_page.html', {
                        'form': form,
                        'name_error': True
                    })
                else:
                    if password == confirm_password:
                        phone_valid = CheckPattern(phone_num)
                        email_valid = CheckPattern(email)
                        password_valid = CheckPattern(password)
                        if phone_valid.check_iranian_phone():
                            if email_valid.check_email_pattern():
                                if password_valid.check_password_letter_number():
                                    user = UserModel(username=name, email=email, phone=phone_num, is_active=False, active_code=create_ranom_code(6))
                                    user.set_password(password)
                                    user.save()
                                    response = send_email(subject="فعال سازی حساب کاربری ", to=user.email, context={"user":user}, template_name="template_service/otp_send_email.html")
                                    if response:
                                        request.session[f'{user.id}otp']=user.email
                                        return redirect(reverse('otp_page', args=[user.id]))
                                    else:
                                        return render(request, 'register_page.html', {
                                            'form' : form,
                                            'error_net': True
                                        })
                                else:
                                    return render(request, 'register_page.html', {
                                        'form': form,
                                        'password_error': True
                                    })
                            else:
                                return render(request, 'register_page.html', {
                                    'form': form
                                })
                        else:
                            return render(request, 'register_page.html', {
                                'form': form,
                                'phone_error': True
                            })
                    else:
                        return render(request, 'register_page.html', {
                            'form': form,
                            'confrim_error': True

                        })
            else:
                return render(request, 'register_page.html', {
                    'form': form,
                    'errors': True
                })
class OtpView(View):
    def get_user(self, email):
        user = UserModel.objects.filter(email=email).last()
        if user is not None:
            return user
        else:
            return False

    def get(self, request:HttpRequest, id):
        otp_session = request.session.get(f'{id}otp')
        if otp_session:
            user = self.get_user(otp_session)
            if user:
                return render(request, 'otp_page.html', {
                    'user_email' : user.email

                })
            else:
                raise Http404
        else:
            raise Http404
    def post(self,request:HttpRequest, id):
        otp_session = request.session.get(f'{id}otp')
        print(id)
        if otp_session:
            user = self.get_user(otp_session)
            if user:
                num1 = request.POST['num1']
                num2 = request.POST['num2']
                num3 = request.POST['num3']
                num4 = request.POST['num4']
                num5 = request.POST['num5']
                num6 = request.POST['num6']
                number = f"{num1}{num2}{num3}{num4}{num5}{num6}"
                print(user.id)
                if number == user.active_code:
                    user.is_active = True
                    user.active_code = create_ranom_code(6)
                    user.save()
                    del request.session[f'{id}otp']
                    return redirect('login_page')
                else:
                    return render(request, 'otp_page.html', {
                        "error" : True

                    })



            else:
                raise Http404
        else:
            raise Http404
class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_page.html', {
            'form': form

        })
    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                email_valid = CheckPattern(email)
                if email_valid.check_email_pattern():
                    user = UserModel.objects.filter(email=email ).last()
                    if user is not None and user.is_active == True:
                        if user.check_password(password):
                            login(request, user)
                            return redirect('home_page')
                        else :
                            return render(request, 'login_page.html', {
                                'form' : form ,
                                "password_error" : True
                            })
                    else:
                        return render(request, 'login_page.html', {
                            'form': form,
                            'user_error'  :True
                        })

                else :
                    return render(request, 'login_page.html', {
                        'form': form,
                        'email_error' : True
                    })
            else :
                return render(request, 'login_page.html', {
                    'form': form,
                    'errors' : True
                })


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home_page')





