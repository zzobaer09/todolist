from django.shortcuts import render , redirect , HttpResponse

# Create your views here.


def Home(response):
    return render(response , "main/home.html" ,{})
