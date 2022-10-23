from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="todolist" , null=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList , on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text
    
