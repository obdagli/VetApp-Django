from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('register/', views.Register, name="Register"),
    path('login/', views.Login, name="Login"),
    path('logout/', views.Logout, name="Logout"),
    path('createpet/', views.CreatePet, name="CreatePet"),
    path('updatepet/<str:pk>/', views.UpdatePet, name="UpdatePet"),
    path('deletepet/<str:pk>/', views.DeletePet, name="DeletePet"),
    path('createowner/', views.CreateOwner, name="CreateOwner"),
    path('updateowner/<str:pk>/', views.UpdateOwner, name="UpdateOwner"),
    path('deleteowner/<str:pk>/', views.DeleteOwner, name="DeleteOwner"),
    path('match/', views.PetOwnerMatch, name="Match"),
    path('updatematched/<str:pk>/', views.UpdateMatched, name="UpdateMatched"),
    path('deletematched/<str:pk>/', views.DeleteMatched, name="DeleteMatched"),
    
]
