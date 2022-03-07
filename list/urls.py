
from django import views
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register('todo',views.TodoListViewSet)

urlpatterns = [
    
    path('customerTodo/<int:pk>',views.CustomerTodo.as_view())
]

urlpatterns += router.urls
    
    

