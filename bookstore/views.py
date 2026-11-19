from rest_framework import filters, permissions, viewsets
from .permissions import EduDomainPermission

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """Публічний довідник авторів: читати може будь-хто. Не змінюйте права тут."""

    queryset = Author.objects.all().order_by("id")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author", "owner")
    serializer_class = BookSerializer
    permission_classes = [EduDomainPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__name"]
    ordering_fields = ["price", "title"]

    def perform_create(self, serializer):
        owner = self.request.user if self.request.user.is_authenticated else None
        serializer.save(owner=owner)
