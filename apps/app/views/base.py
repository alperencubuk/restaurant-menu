from django.db.models import Case, When
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.app.permissions.moderator import IsModerator
from apps.app.serializers.reorder import ReorderSerializer


class BaseModelViewSet(ModelViewSet):
    ordering = ("order", "-id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filterset_fields = {}
        for field in self.get_queryset().model._meta.get_fields():
            if not field.get_internal_type() == "ForeignKey":
                self.filterset_fields[field.name] = self.get_lookup(
                    field.get_internal_type()
                )
        self.filterset_fields.pop("image")

    def get_serializer(self, *args, **kwargs):
        if self.action == "reorder":
            return ReorderSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_permissions(self):
        if self.action in ("retrieve", "list"):
            return (AllowAny(),)
        return (IsModerator(),)

    @action(detail=False, methods=["post"])
    def reorder(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.validated_data.get("order", [])

        cases = [
            When(id=item_id, then=index + 1) for index, item_id in enumerate(order)
        ]

        queryset = self.get_queryset().model.objects.filter(id__in=order)
        queryset.update(order=Case(*cases))

        return Response(
            data={"order": queryset.order_by("order").values_list("id", flat=True)},
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def get_lookup(field_type):
        if field_type in ("CharField", "TextField"):
            return [
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
            ]
        if field_type in (
            "IntegerField",
            "FloatField",
            "DecimalField",
            "DateTimeField",
            "BigAutoField",
        ):
            return ["exact", "lt", "lte", "gt", "gte"]
        return ["exact"]
