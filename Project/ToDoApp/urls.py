from django.urls import path
from .views import *

app_name='ToDoApp'
urlpatterns = [
    path('', ToDoList.as_view(), name='home'),
    path('create/', CreateToDo.as_view(), name='create'),
    path('<slug>', ToDoDetails.as_view(), name='details'),
    path('update/<slug>', ToDoUpdate.as_view(), name='update'),
    path('delete/<slug>', DeleteToDo.as_view(), name='delete'),
]
