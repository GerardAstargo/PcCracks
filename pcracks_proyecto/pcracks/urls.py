from django.contrib import admin
from django.urls import path, include
from .views import menu_off, login

urlpatterns = [
    path('', menu_off, name='menu_off'),
    path('asd', login, name='login'),
]
