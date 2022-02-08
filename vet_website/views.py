from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterOwnerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
@login_required(login_url='register/')
def Home(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        return redirect('register/')
    

def Register(request):
    ownerform = RegisterOwnerForm()
    userform = UserCreationForm()
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        ownerform = RegisterOwnerForm(request.POST)
        if userform.is_valid() and ownerform.is_valid():
            user = userform.save()
            ownerform = ownerform.save(commit=False)
            ownerform.user = user
            ownerform.save()
            username = userform.cleaned_data.get('username')
            messages.success(request, 'User Created Successfully' + username)
            return redirect('Login') 
        
    return render(request, 'login/register.html',{'registerform':ownerform,'userform':userform})

def Login(request):

    if request.method == "POST":
        request.POST.get('username')
        request.POST.get('password')
    return render(request, 'Login',{})