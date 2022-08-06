from django.contrib.auth.models import User
from .models import UserReg
from django.contrib import admin

@admin.register(UserReg)
class PersonAdmin(admin.ModelAdmin):
    pass

def registration(username, email, password, first_name, last_name):

    user = User.objects.create_user(username=username, email=email, password=password)

    user.first_name = first_name
    user.last_name = last_name
    user.save()
