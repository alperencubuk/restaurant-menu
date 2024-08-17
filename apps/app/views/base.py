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
        self.filterset_fields = self.get_filterset_fields()

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

    def get_filterset_fields(self):
        filterset_fields = {}
        filter_exclude = ("image", "qr_code")

        model_meta = self.get_queryset().model._meta

        for field in model_meta.get_fields():
            if field.name in filter_exclude:
                continue

            filterset_fields[field.name] = self.get_lookup(field.get_internal_type())

            if field.get_internal_type() in (
                "ForeignKey",
                "OneToOneField",
                "ManyToManyField",
            ):
                related_model_meta = field.related_model._meta
                for related_field in related_model_meta.get_fields():
                    if related_field.name in ("name", "username"):
                        filterset_fields[f"{field.name}__{related_field.name}"] = (
                            self.get_lookup(related_field.get_internal_type())
                        )

        return filterset_fields

    @staticmethod
    def get_lookup(field_type):
        if field_type in ("CharField", "TextField"):
            return ["exact", "icontains", "istartswith"]
        if field_type in ("IntegerField", "DecimalField", "DateTimeField"):
            return ["exact", "lt", "lte", "gt", "gte"]
        return ["exact"]
