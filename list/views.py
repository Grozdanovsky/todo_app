from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.mixins import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from core.models import User
from core.serializers import UserSerializer

from list.permissions import IsAdminOrReadOnly
from .models import TodoList
from rest_framework.decorators import action
from .serializers import TodoSerializer
# Create your views here.



class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]




class CustomerTodo(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request,pk):  
        customer_todos = TodoList.objects.filter(user = pk)
        serializer = TodoSerializer(customer_todos,many = True)
        return Response(serializer.data)

    
    def delete(self,request,pk):
        customer_todos = TodoList.objects.filter(user = pk).filter(status = 'F')
        customer_todos.delete()
        return Response(f"Item Deleted ", status = status.HTTP_204_NO_CONTENT)
        

# class CustomerViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

    

#     @action(detail=False, methods = ['GET','PUT'], permission_classes = [IsAuthenticated]) # this action is avilable on list view
#     def me(self,request):
#         (customer,created) = User.objects.get_or_create(user_id = request.user.id)
#         if request.method == 'GET':
#             serializer = UserSerializer(customer)
#             return Response(serializer.data)
#         elif request.method == "PUT":
#             serializer = UserSerializer(customer, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)