book.delete()
books = Book.objects.all()
print(books)
#Expected output: <QuerySet []>
#Output: <QuerySet []>