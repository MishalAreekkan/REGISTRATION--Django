from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

def sign(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("cpassword")
        
        print(user_name,password)
        if  not user_name.isalpha():
            return HttpResponse("user name should start with Alphabets")
        
        if len(user_name)<4:
            return HttpResponse("user name should have atleat 4 letters")
        
        if len(password)<2:
            return HttpResponse("pass should have atleast 4 characters")
        
        if password != c_password:
            return HttpResponse("confirm password does not match the password")
        else:
            valid_user = User.objects.create_user(user_name,email,password)
            valid_user.save()
            return redirect("login")
    return render(request,"sign.html")

def login_user(request):
    if request.method == "POST":
        u_name = request.POST.get("username")
        password = request.POST.get("password")
        print(u_name,password)
        login_user = authenticate(request,username= u_name,password = password)
        
        if login_user is not None:
            login(request,login_user)
            return redirect("home")
        else:
            return HttpResponse("username or password is not correct")
  
    return render(request,"login.html")

@login_required(login_url='login')
def home(request):
    if request.User.is_authenticated:
        return render(request, "home.html")

def logout_user(request):
    logout(request)
    return redirect("login")
