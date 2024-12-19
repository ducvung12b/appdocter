from django.shortcuts import render,get_object_or_404,redirect
import os
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
# Login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError  


# Create your views here.
def logoutPage(request):
    logout(request)
    return redirect('viewhome')


def loginPage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:  # Kiểm tra nếu người dùng là admin
            return redirect('admin')  # Điều hướng đến trang admin
        else:
            return redirect('home')  # Điều hướng đến trang chủ người dùng
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:  # Nếu người dùng là admin
                return redirect('admin')  # Điều hướng đến trang admin
            else:
                return redirect('home')  # Điều hướng đến trang chủ người dùng
        else:
            messages.info(request, 'Tài Khoản Đăng Nhập Chưa Đúng..!')

    context = {}
    return render(request, 'app/login.html', context)

# Đăng Ký
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            error = "Tên đăng nhập đã tồn tại."
            return render(request, 'app/register.html', {'error': error})
        
        if User.objects.filter(email=email).exists():
            error = "Email đã tồn tại."
            return render(request, 'app/register.html', {'error': error})

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1,)
            user.save()
            login(request, user)
            return redirect('home')  
        else:
            error = "Mật khẩu không trùng khớp."
            return render(request, 'app/register.html', {'error': error})
    return render(request, 'app/register.html')



def viewhome(request):
    
    return render(request,'app/viewhome.html')

@login_required
def home(request):
    
    return render(request,'app/home.html')