from django.urls import path, re_path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.problems_list, name='index'),
    re_path(r'^problems/(\d+)$', views.problems_detail),
    re_path(r'^problems/$', views.problems_list),
]