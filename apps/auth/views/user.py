from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.auth.serializers.user import (
    CreateUserSerializer,
    MeSerializer,
    UserSerializer,
)


@extend_schema(tags=["user"])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().prefetch_related("restaurants")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        filter_exclude = ("password",)
        self.filterset_fields = [
            field.name
            for field in self.get_queryset().model._meta.get_fields()
            if field.name not in filter_exclude
        ]

    @extend_schema(tags=["me"])
    @action(detail=False, methods=["get", "patch", "delete"])
    def me(self, request):
        self.kwargs["pk"] = request.user.pk
        if request.method == "PATCH":
            return self.partial_update(request)
        if request.method == "DELETE":
            return self.destroy(request)
        return self.retrieve(request)

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return CreateUserSerializer(*args, **kwargs)
        if self.action == "me":
            return MeSerializer(*args, **kwargs)
        return UserSerializer(*args, **kwargs)

    def get_permissions(self):
        if self.action == "create":
            return (AllowAny(),)
        if self.action == "me":
            return (IsAuthenticated(),)
        return (IsAdminUser(),)

    def destroy(self, request, *args, **kwargs):
        """Soft delete user"""
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
