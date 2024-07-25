from django.urls import path, re_path
from . import views
from django.contrib import admin


app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.problems_list),
    re_path(r'^(\d+)$', views.problems_detail),
]
