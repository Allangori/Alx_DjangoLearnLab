from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# The Author model represents an author in the system.
# Each author can have multiple associated books (one-to-many relationship).

# The Book model represents a book, linked to an author via a foreign key.
# It includes fields for title, publication year, and the associated author.
