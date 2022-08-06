from django.forms import ModelForm

from .models import UserReg


class UserRegistrationForm(ModelForm):
    class Meta:
        model = UserReg
        fields = ['username', 'password']
