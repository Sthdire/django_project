from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .admin import registrations






def main_render(request):
    return render(request, 'temp/index.html')


def profile_render(request):
    return render(request, 'temp/profile.html')


def background_render(request):
    return render(request, 'temp/background.html')


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        registrations(username=username, password=password)
        return redirect('/')
    else:
        return render(request, 'auth/reg.html', {})


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "error logging, try again")
            return redirect('/login')
    else:
        return render(request, 'auth/login.html', {})