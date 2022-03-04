from ast import Return
from multiprocessing.spawn import import_main_path
from pprint import pprint
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from .models import Customer,TodoList
from .serializers import CustomerSerializer, TodoSerializer
# Create your views here.

class TodoListView(APIView):
    def get(self,request):
        
        queryset = TodoList.objects.all()
        serializer = TodoSerializer(queryset,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED) 

class TodoListDetail(APIView):
    def get(self,request,pk):
        todo = get_object_or_404(TodoList.objects.all(), pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put (self,request,pk):
        todo = get_object_or_404(TodoList.objects.all(), pk=pk)
        serializer = TodoSerializer(todo,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    
    def delete(self,pk):
        todo = get_object_or_404(TodoList.objects.all(), pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CustomerTodo(APIView):
    def get(self,request,pk):  
        customer_todos = TodoList.objects.filter(customer = pk)
        serializer = TodoSerializer(customer_todos,many = True)
        return Response(serializer.data)
    
    



class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer