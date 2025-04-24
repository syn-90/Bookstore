from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=5, widget=forms.TextInput(attrs={
        'type': "text",  'class': "form-control", 'placeholder': "نام کاربری", 'required': "required", 'name' : "name"}),
        error_messages={
            'required': "نام کاربری اجباری میباشد",
            'min_length' : "نام کاربری شما باید حداقل پنج کارکتر باشد"
        })
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "email", 'class': "form-control", 'placeholder': "ایمیل", 'required': "required", 'name' : "email" }),
    error_messages={
        'invalid': 'لطفا یک ایمیل معتر وارد کنید !!',
        'required': " ایمیل اجباری میباشد"
    })
    phone_number = forms.CharField(widget=forms.TextInput(attrs= {
        'type': "number", 'class': "form-control", 'placeholder':"شماره تماس", 'required': "required", 'name' : "phone_number"}),
    error_messages={
        'required' : "شماره تماس اجباری میباشد"
    })
    password = forms.CharField(max_length=50, min_length=5, widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control", 'id': "toggle_passowrd_field", 'placeholder': "رمز", 'required': "required", 'name' : "password"}),
    error_messages={
        'required': "رمز عبور اجباری میباشد",
        'min_length': "رمز عبور  شما باید حداقل پنج کارکتر باشد"
    })
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type':  "password", 'class': "form-control", 'id': "toggle_passowrd_field02", 'placeholder': "تکرار رمز", 'required': "required", 'name' : "confirm_password"}),
    error_messages={
        'required': "رمز عبور خود را تکرار کنید"
    })

