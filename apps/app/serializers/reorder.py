from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, ListField
from rest_framework.serializers import Serializer


class ReorderSerializer(Serializer):
    order = ListField(
        child=IntegerField(),
        allow_empty=False,
        help_text="A list of IDs to reorder, e.g., [1, 2, 3, 4].",
    )

    @staticmethod
    def validate_order(value):
        if len(value) != len(set(value)):
            raise ValidationError("The list of item IDs must contain unique values.")
        return value
