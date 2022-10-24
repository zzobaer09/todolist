from django.shortcuts import render,redirect
from .forms import SignUpForm
# Create your views here.

def register(response):
    if response.user.is_authenticated:
        return redirect("/profile")
    else:
        if response.method == "POST":
            form = SignUpForm(response.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = SignUpForm()
        return render(response , "register/register.html", {"signup_form":form})

def profile(response):
    if response.user.is_authenticated:
        return render(response , "register/profile.html")
    else: return redirect("/login")

    