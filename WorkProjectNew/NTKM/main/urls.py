from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problems')
router.register(r'users', UserViewSet, basename='users')


app_name = 'main'
urlpatterns = [
    path('register', UserRegister.as_view(), name='Регистрация'),
    path('login', UserLogin.as_view(), name='Вход'),
    path('logout', UserLogout.as_view(), name='Выход'),
    path('user', UserCheckView.as_view(), name='Текущий пользователь'),
    path('', include(router.urls)),
]
