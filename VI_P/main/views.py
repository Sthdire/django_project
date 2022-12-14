from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .admin import registrations


Cheese_cake = ''
Eclair = ''
Napoleon_cake = ''
nap_amount = 0
cheese_amount = 0
eclair_amount = 0
price = 0


def main_render(request):
    return render(request, 'temp/index.html')



def products_render(request):
    global Cheese_cake
    global Eclair
    global Napoleon_cake
    global nap_amount
    global cheese_amount
    global eclair_amount
    global price
    if request.method == "POST":
        if request.POST.get('eclair'):
            Eclair = 'Eclair'
            price += 160
            eclair_amount += 1
        elif request.POST.get('cheese_cake'):
            Cheese_cake = 'Cheese cake'
            price += 210
            cheese_amount += 1
        elif request.POST.get('napoleon_cake'):
            Napoleon_cake = 'Napoleon cake'
            price += 220
            nap_amount += 1

    return render(request, 'temp/products.html')


def basket_render(request):
    global Cheese_cake
    global Eclair
    global Napoleon_cake
    global nap_amount
    global cheese_amount
    global eclair_amount
    global price

    if request.method == "POST":
        address = request.POST['address']
        index = request.POST['index']
        entrance = request.POST['entrance']
        floor = request.POST['floor']
        comment = request.POST['comment']

        if address and index and entrance and floor:
            Cheese_cake, Eclair, Napoleon_cake = "", "", ""
            nap_amount, cheese_amount, eclair_amount, price = 0, 0, 0, 0

            return redirect('/')
        else:
            return redirect('/basket')
    else:
        return render(request, 'temp/basket.html', {'Cheese_cake': Cheese_cake, 'Eclair': Eclair, 'Napoleon_cake': Napoleon_cake, 'price': price, 'nap': nap_amount, 'cheese': cheese_amount, 'eclair': eclair_amount})


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
