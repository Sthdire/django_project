from django.contrib import admin
from django.urls import path, include
from django.utils.termcolors import background

from . import views

urlpatterns = [
    path('', views.main_render),
    path('profile', views.profile_render),
    path('background', views.background_render),
]
