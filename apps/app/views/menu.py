from drf_spectacular.utils import extend_schema

from apps.app.models.menu import Menu
from apps.app.serializers.menu import MenuSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["menu"])
class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all().prefetch_related("categories")
    serializer_class = MenuSerializer
