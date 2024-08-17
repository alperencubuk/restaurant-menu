from django.contrib.auth.models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.app.models.restaurant import Restaurant
from apps.app.serializers.simple import SimpleMenuSerializer
from apps.auth.serializers.simple import SimpleUserSerializer


class RestaurantSerializer(ModelSerializer):
    phone = PhoneNumberField()
    moderators = SerializerMethodField(read_only=True)
    moderator_ids = PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_active=True),
        write_only=True,
        many=True,
        required=False,
        source="moderators",
    )
    menus = SerializerMethodField(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"

    @staticmethod
    def get_moderators(obj) -> SimpleUserSerializer:
        active_moderators = obj.moderators.filter(is_active=True)
        return SimpleUserSerializer(active_moderators, many=True).data

    @staticmethod
    def get_menus(obj) -> SimpleMenuSerializer:
        active_menus = obj.menus.filter(is_active=True)
        return SimpleMenuSerializer(active_menus, many=True).data
