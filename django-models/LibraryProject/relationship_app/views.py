from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def check_role(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


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
    return render(request, 'relationship_app/templates/relationship_app/register.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model =  Library
    template_name = 'relationship_app/templates/relationship_app/library_detail.html'
    context_object_name = 'library'