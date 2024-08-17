from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.category import Category
from apps.app.models.section import Section
from apps.app.serializers.simple import SimpleItemSerializer


class SectionSerializer(ModelSerializer):
    category_id = PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category"
    )
    items = SerializerMethodField(read_only=True)

    class Meta:
        model = Section
        exclude = ("category",)

    @staticmethod
    def get_items(obj) -> SimpleItemSerializer:
        active_items = obj.items.filter(is_active=True)
        return SimpleItemSerializer(active_items, many=True).data
