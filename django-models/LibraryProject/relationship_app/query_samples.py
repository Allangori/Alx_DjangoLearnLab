from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    librarian = Librarian.objects.get(library__name=library_name)
    return librarian
