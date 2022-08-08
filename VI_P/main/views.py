from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .admin import registrations

address = ""
index = ""
entrance = ""
floor = ""
comment = ""

Cheese_cake = 0
Eclair = 0
Napoleon_cake = 0


def main_render(request):
    return render(request, 'temp/index.html')


def profile_render(request):
    return render(request, 'temp/profile.html')


def background_render(request):
    global address
    global index
    global entrance
    global floor
    global comment
    if request.method == "POST":
        address = request.POST['address']
        index = request.POST['index']
        entrance = request.POST['entrance']
        floor = request.POST['floor']
        comment = request.POST['comment']

        if address and index and entrance and floor:
            return redirect('/')
        else:
            return redirect('/background')

    else:
        return render(request, 'temp/background.html', {'values': [Cheese_cake]})


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