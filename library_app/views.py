from rest_framework import viewsets

from library_app.models import Category, Author, Book
from library_app.serializers import CategorySerializer, AuthorSerializer, BookReadSerializer, BookWriteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return BookReadSerializer
        else:
            return BookWriteSerializer
