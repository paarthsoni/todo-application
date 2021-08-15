from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
    path("",views.index,name="home"),
    path("login",views.loginUser,name="login"),
    path("register",views.registerUser,name="register"),
    path("logout",views.logoutUser,name="logout"),
    path("add",views.add,name="add"),
    path("view",views.view,name="view"),
    
]
    