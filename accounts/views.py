from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "accounts/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):

    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid(): 
            user = form.save(commit=False)   
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # کاربر را وارد سیستم می‌کنیم
            return redirect('/')
  
    else:  
        form = SignupForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'accounts/signup.html', context)  