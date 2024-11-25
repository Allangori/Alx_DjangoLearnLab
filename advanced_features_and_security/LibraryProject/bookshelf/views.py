from typing import Any
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        isbn = request.POST['isbn']
        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
        return redirect('book_list')
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})



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
