from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from list.permissions import IsAdminOrReadOnly
from .models import Customer,TodoList
from rest_framework.decorators import action
from .serializers import CustomerSerializer,  TodoSerializer
# Create your views here.



class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

    permission_classes = [IsAdminOrReadOnly]




class CustomerTodo(APIView):
    def get(self,request,pk):  
        customer_todos = TodoList.objects.filter(customer = pk)
        serializer = TodoSerializer(customer_todos,many = True)
        return Response(serializer.data)

    
    def delete(self,request,pk):
        customer_todos = TodoList.objects.filter(customer = pk)
        customer_todos.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == "GET":
            return[AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods = ['GET','PUT'], permission_classes = [IsAuthenticated]) # this action is avilable on list view
    def me(self,request):
        (customer,created) = Customer.objects.get_or_create(user_id = request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)