from django.shortcuts import render, redirect
from django.views import generic

from django.urls import reverse_lazy
from .forms import UserRegisterView
# Create your views here.


def register(request):
     if request.method == 'POST':
        form = UserRegisterView(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/users/login/')
     else:
         form = UserRegisterView()
    

     context = {
        "form":form
        }
     return render(request, 'registration/register.html', context)