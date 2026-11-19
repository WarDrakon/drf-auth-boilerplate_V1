from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=204)


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/v1/auth/token/",
        obtain_auth_token,
        name="api-token-auth",
    ),

    path(
        "api/v1/auth/token/logout/",
        LogoutView.as_view(),
        name="api-token-logout",
    ),

    path("api/v1/", include("bookstore.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)