from django.shortcuts import render , redirect , HttpResponse
from .models import ToDoList
from .forms import NewItem
# Create your views here.


def Home(response):
    return render(response , "main/home.html" ,{})

def list(response):
    if response.user.is_authenticated:
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
                response.user.todolist.add(t_)
                return redirect("/list/{}".format(_name))
        else: form = NewItem()
        return render(response , "main/list.html", {"ls":ls , "form":form})
    
    else: return redirect("/login")

def list_item(response , name):
    t = ToDoList.objects
    all = t.all()
    try:
        t_obj = t.get(name=name , user=response.user.id)
    except: return redirect("/list")
    if t_obj in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                if response.POST.get("item_new"):
                    _item = response.POST.get("item_new")
                    t_obj.item_set.create(text=_item , complete=False)
                for i in t_obj.item_set.all():
                    if response.POST.get("c{}".format(i.id)) == "click":
                        i.complete = True
                    else: i.complete = False
                    i.save()

            for i in t_obj.item_set.all():
                if response.POST.get("d{}".format(i.id)) == "delete":
                    i.delete()
            
            for i in all:
                if response.POST.get("d{}".format(i.id)) == "delete-todo":
                    i.delete()
                    return redirect("/list")
            return redirect("/list/{}".format(name))

        return render(response , "main/list_item.html" , {"ls":t_obj})
    else: return redirect("/list")
