from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.app.models.restaurant import Restaurant
from apps.app.serializers.restaurant import RestaurantSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["restaurant"])
class RestaurantViewSet(BaseModelViewSet):
    queryset = Restaurant.objects.all().prefetch_related("moderators")
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action in ("retrieve", "list"):
            return (AllowAny(),)
        return (IsAdminUser(),)
