from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.item import Item
from apps.app.models.section import Section
from apps.app.serializers.variation import VariationSerializer


class ItemSerializer(ModelSerializer):
    section_id = PrimaryKeyRelatedField(
        queryset=Section.objects.all(), source="section"
    )
    variations = SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        exclude = ("section",)

    @staticmethod
    def get_variations(obj) -> VariationSerializer:
        active_variations = obj.moderators.filter(is_active=True)
        return VariationSerializer(active_variations, many=True).data
