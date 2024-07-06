from django.shortcuts import render
from django.http import HttpResponse
from .models import todo
from .form import TodoForm
from django.shortcuts import redirect
from django.contrib import messages as message
# Create your views here.
def index(request):
    items = todo.objects.all()
    if request.method == 'POST':
        new_item = TodoForm(request.POST)
        new_item.save()
        return redirect('index')
    form = TodoForm()
    page={
        "forms": form,
        "list": items,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)
def delete(request, todo_id):
    item = todo.objects.get(id=todo_id)
    item.delete()
    message.info(request, 'Item deleted')
    return redirect('index')
    