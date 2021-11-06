from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import *


# Create your views here.
def index(request):
    todo_items = To_Do.objects.all().order_by("added_date")

    return render(request, 'todo_app/index.html', {'todo_items': todo_items})

def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_todo = To_Do.objects.create(text = content, added_date = current_date)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    todo = To_Do.objects.get(id = todo_id)
    todo.delete()
    return HttpResponseRedirect('/')