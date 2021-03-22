from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# views.py
from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("=== form valid =====================")
            form.save()
            return redirect("home")
        else:
            print("=== form NOT valid =====================")
            # render(response, "register/register.html", {"form":form})
        # return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})

