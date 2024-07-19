from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Problem, Staff, Sector, ProblemStatus, ProblemType, ObjectOfWork
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def problems_detail(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
    except Problem.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProblemSerializer(problem, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            problem.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
