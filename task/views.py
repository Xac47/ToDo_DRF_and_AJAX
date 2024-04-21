from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tasks
from .serializers import TasksSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tasks-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasks_list(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TasksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return (Response(serializer.data))


@api_view(['POST'])
def task_update(request, pk):
    task = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()

    return Response('Task was deleted!')