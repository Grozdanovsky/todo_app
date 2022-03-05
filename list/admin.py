from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.TodoList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['item','status','customer']
    list_editable = ['status']
    ordering = ['status','customer','item']
    lists_per_page = 10
    
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','birthdate']
    list_editable = ['email','phone']
    search_fields = ['first_name__istartswith','last_name__istartswith']
    lists_per_page = 10
    ordering = ['first_name','last_name']
    