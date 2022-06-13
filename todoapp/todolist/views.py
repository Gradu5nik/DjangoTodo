from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo
# Create your views here.


def index(request):
    todolist = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todolist})


@require_http_methods(["POST"])
def add(request):
    # this title seems to be name of html input field
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
