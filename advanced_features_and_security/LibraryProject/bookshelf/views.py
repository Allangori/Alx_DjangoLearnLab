from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Book
from django.contrib.auth.decorators import login_required, user_passes_test


class BookUpdateView(UpdateView):
  model = Book
  fields = ['title', 'author', 'description']
  template_name = 'books/book_update_form.html'
  success_url = reverse_lazy('book_list')

  def form_valid(self, form):
    response = super().form_valid(form) 
    return response

def hello_view(request):
    return HttpResponse("Welcome to my website!")
class Hello_TemplateView(TemplateView):
    template_name = "hello_view.html"
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def  get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.get_average_rating()



def is_librarian(user):
    return user.groups.filter(name="Librarians").exists()

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Welcome, Librarian!")



def role_required(role):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user.userprofile.role != role:
                return HttpResponseForbidden("You do not have access.")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

@role_required("Member")
def member_dashboard(request):
    return HttpResponse("Welcome, Member!")
