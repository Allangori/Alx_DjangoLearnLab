from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # Import your views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the BookViewSet


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
