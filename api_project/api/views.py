from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
# from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#class IsAdminOrReadOnly(BasePermission):
    #def has_permission(self, request, view):
        #if request.method in ['GET', 'HEAD', 'OPTIONS']:
            #return True
        #return request.user and request.user.is_staff
#permission_classes = [IsAdminOrReadOnly]