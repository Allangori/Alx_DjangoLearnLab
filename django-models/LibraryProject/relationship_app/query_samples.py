from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author,  author_name):
    books = Author.objects.get(name=author_name),
    objects.filter(author = author)
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    librarian = Librarian.objects.get(library__name=library_name)
    return librarian
