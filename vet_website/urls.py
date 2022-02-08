from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('register/', views.Register, name="Register"),
    path('login/', views.Login, name="Login"),
]
