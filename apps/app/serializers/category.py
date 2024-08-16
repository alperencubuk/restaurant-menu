from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.category import Category
from apps.app.models.menu import Menu


class CategorySerializer(ModelSerializer):
    menu_id = PrimaryKeyRelatedField(queryset=Menu.objects.all(), source="menu")

    class Meta:
        model = Category
        exclude = ("menu",)
