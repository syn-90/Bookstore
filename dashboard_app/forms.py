from django.forms import forms

class ChangePasswordForm(forms.Form):
    username = forms.Charfield(max_lentgh = 50 , min_lentgh = 4 , widget = forms.TextInput(attrs = {

    }))