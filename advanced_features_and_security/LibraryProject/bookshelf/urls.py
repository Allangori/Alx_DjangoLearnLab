from django.contrib import admin
from django.urls import path
from .models import views
from LibraryProject import settings.INS

urlpatterns = [
    path( 'hello/', views.hello_view, name= 'greetings'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',
             TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
]