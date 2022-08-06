from django.contrib.auth.models import User
from .models import UserReg
from django.contrib import admin

@admin.register(UserReg)
class PersonAdmin(admin.ModelAdmin):
    pass

def registrations(username, password):

    user = User.objects.create_user(username=username, password=password)
    user.save()
