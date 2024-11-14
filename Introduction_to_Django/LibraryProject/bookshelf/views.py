from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Book

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