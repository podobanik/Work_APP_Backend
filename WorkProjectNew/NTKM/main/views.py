from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


from .permissions import IsAdminOrIsOwner
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, generics, viewsets
from .models import Problem, AppUser


class ProblemViewSet(viewsets.ModelViewSet):
    serializer_class = ProblemSerializer
    permission_classes = (IsAdminOrIsOwner, )
    authentication_classes = (SessionAuthentication, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Problem.objects.all()

        return Problem.objects.filter(pk=pk)

    # @action(methods=['get'], detail=True)
    # def person(self, request, pk=None):
    #     staff = Staff.objects.get(pk=pk)
    #     return Response({'staff': staff.staff_name, 'sector_id': staff.sector_id})


class AppUserViewSet(viewsets.ModelViewSet):
    serializer_class = AppUserSerializer
    permission_classes = (IsAdminOrIsOwner, )
    authentication_classes = (SessionAuthentication, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk: 
            return AppUser.objects.all()

        return AppUser.objects.filter(pk=pk)
