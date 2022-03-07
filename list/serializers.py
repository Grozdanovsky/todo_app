from rest_framework import serializers

from list.models import  TodoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id','item','status','user']

