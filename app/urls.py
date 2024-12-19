from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # View
    path('home/', views.home,name='home'),
    path('', views.viewhome,name='viewhome'),

    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.register,name='register'),
]