from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path( 'hello/', views.hello_view, name= 'greetings')
]