from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():#cheaking for the availiablity of username
            messages.info(request,'used not exist please signup')
            return redirect("login_page")
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'credential doesnot match')
            return redirect("login_page")
        else:
            login(request,user)
            messages.info(request,'loged in successful!')
            return redirect("home")

    return render(request,"login_page.html")





def signup_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name",'')
        username=request.POST.get("username")
        password=request.POST.get("password")
        profile_photo = request.FILES.get("profile_photo")
        
        user_valid=User.objects.filter(username=username)
        if user_valid:#cheaking for the availiablity of username
            messages.info(request,'username already exist please change the username')
            return redirect("signup_page")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        UserProfileModel.objects.create(user=user, profile_photo=profile_photo)

        messages.info(request,'registration successful')
        return redirect("login_page")

    return render(request,"signup_page.html")


def logout_page(request):
    logout(request)   
    return redirect("home")