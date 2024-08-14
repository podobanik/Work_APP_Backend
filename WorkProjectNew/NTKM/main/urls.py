from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problems')
router.register(r'staff', StaffViewSet, basename='staff')


app_name = 'main'
urlpatterns = [
    path('', include(router.urls)),
]
