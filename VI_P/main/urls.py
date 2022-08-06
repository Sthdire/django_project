from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main_render),
    path('profile', views.profile_render),
    path('background', views.background_render),

]
# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('registration', views.registration),
]


