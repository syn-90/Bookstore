from django.http import Http404
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import *
# Create your views here.
from django.views.generic import View


class ContactView(View):
    def get(self, request):
        if request.method == 'GET':
            form = ContactForm()
            return render(request, 'contact_page.html', {
                'form': form
            })
        # else:
        #     raise Http404

    def post(self, request):
        if request.method == 'POST':

            form = ContactForm(request.POST)
            if form.is_valid():

                neme = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                message = form.cleaned_data.get('message')
                new_message = ContactModel(name=neme, email=email, message=message)
                new_message.save()
                return redirect('home_page')
            else:
                return render(request, 'contact_page.html', {
                    'form': form,
                    'errors': True
                })
        # else:
        #     raise Http404

# try:
#     def get(self, request):
#         if request.method == 'GET':
#             form = ContactForm()
#             return render(request, 'contact_page.html', {
#                 'form':form
#             })
#         elif request.method == 'POST':
#
#             form = ContactForm(request.POST)
#             neme = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             message = form.cleaned_data.get('message')
#
#             if form.is_valid():
#                 new_message = ContactModel(name=neme, email=email, message=message)
#                 new_message.save()
#             else:
#                 return render(request, 'contact_page.html', {
#                     'form': form
#                 })
# except:
#     def get(self, request):
#         return render(request, 'home_page.html', {
#
#         })

# def contact_us(request):
#     if request.method == 'GET':
#         form = ContactForm()
#         return render(request, 'contact_page.html', {
#             'form': form
#         })
#     elif request.method == 'POST':
#         form = ContactForm(request.POST)
#         neme = form.cleaned_data.get('name')
#         email = form.cleaned_data.get('email')
#         message = form.cleaned_data.get('message')
#         if form.is_valid():
#
#             new_message = ContactModel(name=neme, email=email, message=message)
#             new_message.save()
#             return redirect('home_page')
#         else:
#             return render(request, 'contact_page.html', {
#                 'form': form
#             })
