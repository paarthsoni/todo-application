from django.http.response import HttpResponse
from todo.models import tasks, userdetails
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from todo.models import userdetails,tasks

def index(request):
    return render(request,"index.html")

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Your are logged in successfully')
            return redirect("/",username)
            
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect("/login")
    
    return render(request,"login.html")

def registerUser(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("username")
        email=request.POST.get("emailid")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if cpassword==password and username is None:
            user = User.objects.create_user(username=username,email=email,password=password)
            userdata=userdetails(fname=fname,lname=lname,username=username,email=email,date=datetime.today())
            user.save()
            userdata.save()
            login(request,user)
            messages.success(request, 'Your account is created successfully ')
            return redirect("/")
        elif cpassword!=password:
            messages.warning(request, 'Entered passwords do not match!!')
            return redirect("/register")
        elif username is not None:
            messages.warning(request, 'Username already exists!! Please enter a different username')
            return redirect("/register")


    return render(request,"register.html")

def logoutUser(request):
   logout(request)
   messages.success(request, 'Logged out Successfully ')
   return redirect("/")

def add(request):
    if request.method=="POST":
        username=get_user(request)
        taskdetail=request.POST.get("taskdetail")
        userdata=tasks(task=taskdetail,username=username,date=datetime.now())
        userdata.save()
        messages.success(request, 'Task added successfully!!')
        return redirect("/add")
    return render(request,"add.html")

def deletedata(request,id):
    tasks.objects.filter(id=id).delete()
    username=get_user(request)
    data=tasks.objects.filter(username=username)
    return render(request,"view.html",{'data': data})


    

def view(request):
        username=get_user(request)
        data=tasks.objects.filter(username=username)
        return render(request,"view.html",{'data': data})
    
    

