from rest_framework import serializers

from task.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
