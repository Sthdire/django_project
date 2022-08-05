from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_render),
    path('profile', views.profile_render),
    path('background', views.background_render),
]
