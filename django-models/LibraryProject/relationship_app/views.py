from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = 'logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model =  Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'