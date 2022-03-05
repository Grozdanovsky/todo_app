from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import *
from .models import Customer,TodoList
from .serializers import CustomerSerializer,  TodoSerializer
# Create your views here.



class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer





class CustomerTodo(APIView):
    def get(self,request,pk):  
        customer_todos = TodoList.objects.filter(customer = pk)
        serializer = TodoSerializer(customer_todos,many = True)
        return Response(serializer.data)

    
    def delete(self,request,pk):
        customer_todos = TodoList.objects.filter(customer = pk)
        customer_todos.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

class CustomerViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer