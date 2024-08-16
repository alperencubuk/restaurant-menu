from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.menu import Menu
from apps.app.models.restaurant import Restaurant


class MenuSerializer(ModelSerializer):
    restaurant_id = PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source="restaurant"
    )

    class Meta:
        model = Menu
        exclude = ("restaurant",)
