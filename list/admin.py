from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.TodoList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['item','status','user']
    list_editable = ['status']
    ordering = ['status','user','item']
    lists_per_page = 10
    
