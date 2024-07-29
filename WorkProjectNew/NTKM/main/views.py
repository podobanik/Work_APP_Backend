from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Problem


@api_view(['GET', 'POST'])
def problems_list(request):
    if request.method == 'GET':
        data = Problem.objects.all()
        serializer = ProblemSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.validated_data
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def problems_detail(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
    except Problem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProblemSerializer(problem, data=request.data, context={'request': request})
        if serializer.is_valid():
            #serializer.validated_data
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        problem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
