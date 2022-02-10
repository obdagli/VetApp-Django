from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
from itertools import chain
# Create your views here.
def Home(request):
    pets = Pet.objects.all()
    owners = Owner.objects.all()
    matched = PetOwnerMatching.objects.all()
    context={'pets':pets,'owners':owners,'matched':matched}
    return render(request,'home.html',context)
    

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login/login.html',{})

def Logout(request):
    logout(request)
    return redirect('Home')

def CreatePet(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Created Successfully')
    return render(request, 'pet/createpet.html',{'form':form})

def PetOwnerMatch(request):
    form = PetOwnerMatchForm()
    if request.method == "POST":
        form = PetOwnerMatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Matching Successfully')

    owner = Owner.objects.all()
    pet = Pet.objects.all()
    return render(request, 'match/match.html',{'owners':owner,'pets':pet,'form':form})

def UpdateMatched(request, pk):
    matched = PetOwnerMatching.objects.get(id=pk)
    form = PetOwnerMatchForm(instance=matched)
    if request.method == "POST":
        form = PetOwnerMatchForm(request.POST, instance=matched)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Matching Updated Successfully')
            return redirect('Home')
    context = {'form':form}
    return render(request, 'match/match.html',context)

def DeleteMatched(request, pk):
    matched = PetOwnerMatching.objects.get(id=pk)
    if request.method == "POST":
        matched.delete()
        messages.success(request, 'Pet Matching Deleted Successfully')
        return redirect('Home')
    context = {'item':matched}
    return render(request, 'delete/delete.html',context)

def UpdatePet(request, pk):
    pet = Pet.objects.get(id=pk)
    form = PetForm(instance=pet)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet Updated Successfully')
            return redirect('Home')
    context = {'form':form}
    return render(request, 'pet/createpet.html',context)

def DeletePet(request, pk):
    pet = Pet.objects.get(id=pk)
    if request.method == "POST":
        pet.delete()
        messages.success(request, 'Pet Deleted Successfully')
        return redirect('Home')
    context = {'item':pet}
    return render(request, 'delete/delete.html',context)