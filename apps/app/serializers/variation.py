from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.item import Item
from apps.app.models.variation import Variation


class VariationSerializer(ModelSerializer):
    item_id = PrimaryKeyRelatedField(queryset=Item.objects.all(), source="item")

    class Meta:
        model = Variation
        exclude = ("item",)
