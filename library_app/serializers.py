from rest_framework import serializers

from library_app.models import Category, Book, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
