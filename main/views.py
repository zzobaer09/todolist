from django.shortcuts import render , redirect , HttpResponse

# Create your views here.


def Home(responser):
    return render(responser , "main/home.html")
