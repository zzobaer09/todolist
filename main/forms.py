from django import forms


class NewItem(forms.Form):
    todolist = forms.CharField(max_length=255 , label="name")
    item = forms.CharField(max_length=1000 , label="item")
    complete = forms.BooleanField(label="complete" , required=False)