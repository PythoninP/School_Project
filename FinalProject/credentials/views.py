from email import message

from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def Hlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new.html')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('Hlogin')
    return render(request, "Hlogin.html")


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('new')
    return render(request, "login.html")


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.create_user(username=username, email=email)
        user.save();

        return redirect('new')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):

    return render(request, 'new.html')

def registration(request):

    return render(request, 'registration.html')

def order(request):
    return render(request, 'order.html')