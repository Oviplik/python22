from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('exc2',views.exc2,name='exercise2'),
    path('exc4',views.exc4,name='exercise4'),
]