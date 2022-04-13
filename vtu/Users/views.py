from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreationForm
from paystack.models import Payment
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout as django_logout
from django.utils.safestring import mark_safe





# Create your views here.
def register(request):
    form=CreationForm()
    if request.method == 'POST':
        form =CreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["email"]} registered succesfully!, procced to login' )
    context ={
        'form':form,
        'title':'SameDeal | Register'
        }
    return render (request , "register.html",  context)
        
   


def Login(request):
    
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as {request.user.username}'))
        return redirect('dashboard')
    
    username =""
    
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        remember_me =request.POST.get('remember_me')
        user=authenticate(request, username=username, password=password )
        if user:
            login(request, user)
            messages.success(request, f'User {user.username} logged in succesfully!')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('dashboard')
        else:
            messages.warning(request, 'could not authenticate, check credentials.')
    context={
        'title':'SameDeal | Login',
        "username":username
        
    }
    return render (request , "Login.html", context)
         
def logout(request):
    django_logout(request)
    messages.success(request, 'Logged out successfully')
    return render(request, 'logout.html') 
   
def reset(request):
    
    return render(request, 'reset.html')    

def dashboard(request):
    
    balance = Payment.amount

    
    
    
    context = {
        'balance':balance
        
    }
    return render(request, 'dashboard.html', context)


def transaction(request):
   
    return render(request, 'transactions.html')