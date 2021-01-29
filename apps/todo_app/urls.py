
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('add', views.addTodoItems),
  path('completed/<todo_id>', views.completedTodo),
  path('deletecompleted', views.deleteCompleted),
  path('deleteall', views.deleteAll),

]
