from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main_render),
    path('products', views.products_render),
    path('basket', views.basket_render),
]
# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('reg', views.registration),
    path('login', views.login_page),
    path('logout', views.logout_page),
]


