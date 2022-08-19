from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo1, name='demo1'),
    path('add', views.add, name='add'),
]