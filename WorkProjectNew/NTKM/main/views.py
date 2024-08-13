from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, generics, viewsets
from .models import Problem, Staff


class ProblemViewSet(viewsets.ModelViewSet):
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Problem.objects.all()

        return Problem.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def person(self, request, pk=None):
        staff = Staff.objects.get(pk=pk)
        return Response({'staff': staff.staff_name})

