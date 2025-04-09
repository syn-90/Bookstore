from django import forms
from .models import ContactModel


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactModel
#         fields = ['name', 'email', 'message']
#         widgets = {
#             'name':forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' :"form-control", 'type':"text", 'id':"name", 'name':"name", 'required':"required"})),
#             'email':forms.EmailField(widget=forms.EmailInput(attrs={'class' :"form-control", 'type':"email", 'id':"email", 'name':"email", 'required':"required"})),
#             'message': forms.CharField(widget=forms.Textarea(attrs={'class' :"form-control", 'id' : "message",  'name':"message", 'rows':"5",'placeholder': "پیام خودرا یادداشت کنید" }))
#
#         }
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': "form-control", 'type': "text", 'id': "name", 'name': "name", 'required': "required", 'minlength' : '5'
    }),
        error_messages={
            'required' : 'نام و نام خانوادگی اجباری است ',
            'minlength': 'نام و نام خانوادگی حداقل پنج کارکتر باشد '
        })
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control", 'type': "email", 'id': "email", 'name': "email", 'required': "required"
    }),
    error_messages={
        'required': 'ایمیل اجباری است ',
        'invalid' : 'لطفا یک ایمیل معتر وارد کنید !!'

    })
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control", 'id': "message", 'name': "message", 'rows': "5",
        'placeholder': "پیام خودرا یادداشت کنید"
    }))
