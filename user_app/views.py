from django.shortcuts import render, redirect
from django.views import View
from .models import UserModel
from .forms import RegisterForm
from utils.check_pattern import CheckPattern


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_page.html', {
            'form': form

        })

    def post(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("name")
                email = form.cleaned_data.get("email")
                phone_num = form.cleaned_data.get("phone_number")
                password = form.cleaned_data.get("password")
                confirm_password = form.cleaned_data.get("confirm_password")
                if password == confirm_password:
                    phone_valid = CheckPattern(phone_num)
                    email_valid = CheckPattern(email)
                    password_valid = CheckPattern(password)
                    if phone_valid.check_iranian_phone():
                        if email_valid.check_email_pattern():
                            if password_valid.check_password_letter_number():
                                user = UserModel(username=name, email=email, phone=phone_num, is_active=False)
                                user.set_password(password)
                                user.save()
                                return redirect("home_page")
                            else:
                                return render(request, 'register_page.html', {
                                    'form' : form,
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
                        'confrim_error' : True


                    })
            else:
                return render(request, 'register_page.html', {
                    'form': form,
                    'errors': True
                })