
from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author",
        write_only=True
    )

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        allow_null=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "author_id",
            "price",
            "cover",
            "owner"
        ]
        read_only_fields = ["cover", "owner"]
