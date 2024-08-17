from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.category import Category
from apps.app.models.menu import Menu
from apps.app.serializers.simple import SimpleSectionSerializer


class CategorySerializer(ModelSerializer):
    menu_id = PrimaryKeyRelatedField(queryset=Menu.objects.all(), source="menu")
    sections = SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        exclude = ("menu",)

    @staticmethod
    def get_sections(obj) -> SimpleSectionSerializer:
        active_sections = obj.sections.filter(is_active=True)
        return SimpleSectionSerializer(active_sections, many=True).data
