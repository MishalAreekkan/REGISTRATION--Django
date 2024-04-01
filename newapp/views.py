from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def sign(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("cpassword")
        if password != c_password:
            return HttpResponse("confirm password does not match the password")
        else:
            valid_user = User.objects.create_user(user_name,email,password)
            valid_user.save()
            return redirect("login")
    print('llk')
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

def home(request):
    return render(request,"home.html")
