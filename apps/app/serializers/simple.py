from rest_framework.serializers import ModelSerializer

from apps.app.models.category import Category
from apps.app.models.item import Item
from apps.app.models.menu import Menu
from apps.app.models.restaurant import Restaurant
from apps.app.models.section import Section


class SimpleRestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name")


class SimpleMenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "name")


class SimpleCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class SimpleSectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "name")


class SimpleItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name")
