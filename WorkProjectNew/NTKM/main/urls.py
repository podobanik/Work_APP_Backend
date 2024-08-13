from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problems')
print(router.urls)

app_name = 'main'
urlpatterns = [
    path('', include(router.urls)),
]
