from django.shortcuts import render

from apps.todo_app.models import TodoList

from apps.todo_app.forms import TodoListForm

# Create your views here.


def index(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodoListForm()
    context = {
        'items': todo_items, 
        'form': form,
    }
    return render(request, 'todo_html/index.html', context)
