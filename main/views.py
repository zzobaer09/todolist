from django.shortcuts import render , redirect , HttpResponse
from .models import ToDoList
from .forms import NewItem
# Create your views here.


def Home(response):
    return render(response , "main/home.html" ,{})

def list(response):
    t = ToDoList.objects
    ls = t.all()

    if response.method == "POST":
        form = NewItem(response.POST)
        print(response.POST)

        if form.is_valid():
            _name = form.cleaned_data["todolist"]
            _item = form.cleaned_data["item"]
            _complete = form.cleaned_data["complete"]
            t_ = ToDoList(name=_name)
            t_.save()
            t_.item_set.create(text=_item , complete=_complete)
            redirect("/list")
    else: form = NewItem()
    return render(response , "main/list.html", {"ls":ls , "form":form})
