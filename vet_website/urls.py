from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('register/', views.Register, name="Register"),
    path('login/', views.Login, name="Login"),
    path('logout/', views.Logout, name="Logout"),
    path('createpet/', views.CreatePet, name="CreatePet"),
    path('pets/', views.PetCard, name="Pets"),
    path('match/', views.PetOwnerMatch, name="Match"),
]
