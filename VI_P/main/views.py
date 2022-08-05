from django.shortcuts import render


def main_render(request):
    return render(request, 'temp/index.html')

def profile_render(request):
    return render(request, 'temp/profile.html')

def background_render(request):
    return render(request, 'temp/background.html')

def login(request):
    return render(request, 'temp/login.html')

def reg(request):
    return render(request, 'temp/reg.html')