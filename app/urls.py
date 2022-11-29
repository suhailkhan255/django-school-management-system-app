from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
]