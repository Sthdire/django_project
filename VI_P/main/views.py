from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def main_render(request):
    return render(request, 'temp/index.html')


def profile_render(request):
    return render(request, 'temp/profile.html')


def background_render(request):
    return render(request, 'temp/background.html')


def registration(request):
    user_form = UserRegistrationForm
    if request.method == 'POST':
        user_form = user_form(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Save the User object
            new_user.save()
            return redirect('/')
        else:
            user_form = UserRegistrationForm()
    return render(request, 'registration/reg.html', context={'user_form': user_form})
