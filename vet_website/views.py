from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def Home(request):
    pets = Pet.objects.all()
    owners = Owner.objects.all()
    matched = PetOwnerMatching.objects.all()
    petidsgroupedbyownerid = PetOwnerMatching.objects.values('ownerid').annotate('petid')
    print(petidsgroupedbyownerid) 
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

def PetCard(request):
    pet = Pet.objects.all()
    return render(request, 'cards/pets.html',{'pets':pet})

def PetOwnerMatch(request):
    form = PetOwnerMatchForm()
    if request.method == "POST":
        form = PetOwnerMatchForm(request.POST)
        if form.is_valid():
            ownerid = request.POST["ownerid"]
            petid = request.POST["petid"]
            print(ownerid)
            print(petid)
            form.save()
            messages.success(request, 'Pet Matching Successfully')

    owner = Owner.objects.all()
    pet = Pet.objects.all()
    return render(request, 'match/match.html',{'owners':owner,'pets':pet,'petform':form})