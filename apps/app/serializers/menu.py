from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.menu import Menu
from apps.app.models.restaurant import Restaurant
from apps.app.serializers.simple import SimpleCategorySerializer


class MenuSerializer(ModelSerializer):
    restaurant_id = PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source="restaurant"
    )
    categories = SerializerMethodField(read_only=True)

    class Meta:
        model = Menu
        exclude = ("restaurant",)

    @staticmethod
    def get_categories(obj) -> SimpleCategorySerializer:
        active_categories = obj.categories.filter(is_active=True)
        return SimpleCategorySerializer(active_categories, many=True).data
