from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerFarmer(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_farmer = True
            user.is_buyer = False
            user.set_password(request.POST['password'])
            user.save()
            
            return redirect('home')
    
    return render(request, 'users/registerFarmer.html', {'form' : form})

def registerBuyer(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_farmer = False
            user.is_buyer = True
            user.set_password(request.POST['password'])
            user.save()
            
            return redirect('login')
    
    return render(request, 'users/registerBuyer.html', {'form' : form})

def loginView(request):
    error_message = 0
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials'
    return render(request, 'users/login.html', {'errors' : error_message})

def logoutView(request):
    logout(request)
    return redirect('login')