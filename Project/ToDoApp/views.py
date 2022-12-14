from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django import forms
import datetime
from django.db.models import Q
# Create your views here.
class CreateToDo(CreateView):
    model = ToDo
    template_name = "ToDoApp/todo_form.html"
    fields = ['title', 'description', 'tools', 'daycount', 'endgoal', 'due']

class ToDoList(ListView):
    model = ToDo
    context_object_name = 'tasks'
    template_name= 'ToDoApp/home.html'
    
    extra_context = {'due' : datetime.datetime(2022, 10, 30)}
    
    def get_queryset(self):
        q = self.request.GET.get('q', '')
        multiple_search = Q(Q(title__icontains=q) | Q(tools__icontains=q))
        tasks = ToDo.objects.filter(multiple_search)
        
        return tasks
    

    
class ToDoDetails(DetailView):
    model = ToDo
    template_name='ToDoApp/details.html'
    context_object_name = 'task_detail'
    
class ToDoUpdate(UpdateView):
    model =ToDo
    fields = ['title', 'description', 'tools', 'daycount', 'endgoal', 'due']
    
class DeleteToDo(DeleteView):
    model = ToDo
    template_name = "ToDoApp/delete.html"
    success_url = reverse_lazy("ToDoApp:home")
    context_object_name = 'task'

