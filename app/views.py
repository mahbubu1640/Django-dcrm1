from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages


def home_view(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # authentication 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect("home")
        else:
            messages.error(request,"Error In Logging! Please Enter valid Email and Password")
            return redirect("home")
    else:
        return render(request,"home.html")



def register_view(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]    
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered")
            return redirect("home")
        else:
            messages.error(request,"enter Valid Data")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request,"register.html",{"form":form})
                    
    
    


def logout_view(request):
    logout(request)
    messages.success(request,"You have been Logged Out")
    return redirect('home')