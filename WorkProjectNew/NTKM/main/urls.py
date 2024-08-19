from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problems')
router.register(r'users', AppUserViewSet, basename='users')


app_name = 'main'
urlpatterns = [
    path('', include(router.urls)),
]
