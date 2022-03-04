from rest_framework import serializers

from list.models import Customer, TodoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id','item','status','customer']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Customer
        fields = ['id','first_name','last_name','email','phone','birthdate']