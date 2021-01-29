from django.shortcuts import render, redirect

from apps.todo_app.models import TodoList

from apps.todo_app.forms import TodoListForm

from django.views.decorators.http import require_POST   
# Create your views here.


def index(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodoListForm()
    context = {
        'items': todo_items, 
        'form': form,
    }
    return render(request, 'todo_html/index.html', context)

@require_POST
def addTodoItems(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()

    print(request.POST['text'])
    return redirect('index')

def completedTodo(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    TodoList.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    TodoList.objects.all().delete()

    return redirect('index')
