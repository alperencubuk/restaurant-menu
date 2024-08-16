from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.category import Category
from apps.app.models.section import Section


class SectionSerializer(ModelSerializer):
    category_id = PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category"
    )

    class Meta:
        model = Section
        exclude = ("category",)
