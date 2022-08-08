from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .admin import registrations

address = ""
index = ""
entrance = ""
floor = ""
comment = ""

Cheese_cake = ''
Eclair = ''
Napoleon_cake = ''


def main_render(request):
    return render(request, 'temp/index.html')


def profile_render(request):
    global Cheese_cake
    global Eclair
    global Napoleon_cake
    if request.method == "POST":
        if request.POST.get('eclair'):
            Eclair = 'Eclair'
        elif request.POST.get('cheese_cake'):
            Cheese_cake = 'Cheese cake'
        elif request.POST.get('napoleon_cake'):
            Napoleon_cake = 'Napoleon cake'

    return render(request, 'temp/profile.html')


def background_render(request):
    global Cheese_cake
    global Eclair
    global Napoleon_cake

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
        return render(request, 'temp/background.html', {'Cheese_cake': Cheese_cake, 'Eclair': Eclair, 'Napoleon_cake': Napoleon_cake})


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


def logout_page(request):
    logout(request)
    return render(request, 'temp/index.html')
