from django.shortcuts import render,redirect
from django import forms 
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import RecordForm


def home_view(request):
    record = Record.objects.all()
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # now use this username and password for login 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request,"Error!! Enter Valid username and password")
            return redirect("home")
    else:
        return render(request,"home.html",{'record':record})

def register_view(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Registered Successfully !!!")
            return redirect("home")
        else:
            messages.error(request,"Error!!! Please Enter Correct Data")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request,"register.html",{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,"You have been log out !!!")
    return redirect("home")


def detail_view(request,pk):
    record = Record.objects.get(pk=pk)
    return render(request,"detail.html",{'record':record})

def update_view(request,pk):
    record = Record.objects.get(pk=pk)
    form = RecordForm(instance=record)
    if request.method=="POST":
        form = RecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Employee Record Successfully")
            return redirect("home")
        else:
            messages.error(request,"Error !!! Enter Valid Data")
            return redirect("home")
    else:
        return render(request,"update.html",{'form':form})
  

def delete_view(request,pk):
    record = Record.objects.get(pk=pk)
    record.delete()
    messages.success(request,"Employee Record Deleted Successfully")
    return redirect("home")

def add_record(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = RecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Employee Added Successfully")
                return redirect("home")
            else:
                messages.error(request,"Error ! Enter valid data")
                return redirect("home")
        else:
            form = RecordForm()
            return render(request,"add_record.html",{'form':form})
    else:
        messages.error(request,"You must have to Logged In to add Employee Record")
        return redirect("home")
