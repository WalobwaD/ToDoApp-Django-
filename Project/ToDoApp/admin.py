from django.contrib import admin
from .models import *
# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'daycount')
    ordering = ('id',)

admin.site.register(ToDo, ToDoAdmin)