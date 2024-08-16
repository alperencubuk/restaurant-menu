from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from apps.app.serializers.simple import SimpleRestaurantSerializer


class UserSerializer(ModelSerializer):
    restaurants = SimpleRestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = "__all__"

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class MeSerializer(UserSerializer):
    class Meta:
        model = User
        read_only_fields = (
            "username",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "restaurants",
            "groups",
            "user_permissions",
        )
        extra_kwargs = {"password": {"write_only": True}}
        fields = "__all__"


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = ("username", "password", "first_name", "last_name", "email")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
