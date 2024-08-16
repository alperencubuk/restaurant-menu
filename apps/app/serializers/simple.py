from rest_framework.serializers import ModelSerializer

from apps.app.models.restaurant import Restaurant


class SimpleRestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name")
