from rest_framework.permissions import BasePermission, SAFE_METHODS


class EduDomainPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        email = request.user.email.lower()

        domain = email.rsplit("@", 1)[-1]

        return domain.endswith(".edu.ua")