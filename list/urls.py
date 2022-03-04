
from django import views
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register('customer',views.CustomerViewSet)

urlpatterns = [
    path('todo/',views.TodoListView.as_view()),
    path('todo/<int:pk>',views.TodoListDetail.as_view()),
    path('customerTodo/<int:pk>',views.CustomerTodo.as_view())
]

urlpatterns += router.urls
    
    

