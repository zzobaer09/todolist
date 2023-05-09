from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Home , name="home"),
    path("list/" , views.list , name="list"),
    path("list/<str:name>/" ,views.list_item , name="list item"),
]
