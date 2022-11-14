from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','start_date','end_date','completed']