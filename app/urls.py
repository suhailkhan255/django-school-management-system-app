from django.contrib import admin
from django.urls import path

from .import views, Hod_Views

urlpatterns = [
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('Hod/Home',Hod_Views.HOME, name='hod_home'),
    path('doLogout',views.doLogout,name='logout'),



]