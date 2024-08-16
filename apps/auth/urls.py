from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views.user import UserViewSet
from config.core import Router

router = Router()

router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r"login/?$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    re_path(r"refresh/?$", TokenRefreshView.as_view(), name="token_refresh"),
]
