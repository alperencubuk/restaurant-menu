from drf_spectacular.utils import extend_schema

from apps.app.models.item import Item
from apps.app.serializers.item import ItemSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["item"])
class ItemViewSet(BaseModelViewSet):
    queryset = Item.objects.all().prefetch_related("variations")
    serializer_class = ItemSerializer
