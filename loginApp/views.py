from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
import crypt


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'loginApp/index.html')


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'loginApp/register.html')

class CreateUser(View):
    def post(self, request, *args, **kwargs):

        User.objects.create(username=request.POST.get('username'),
                            password=crypt.crypt(request.POST.get('password')))

        return redirect('auth:index')
