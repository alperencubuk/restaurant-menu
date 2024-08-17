from drf_spectacular.utils import extend_schema

from apps.app.models.menu import Menu
from apps.app.serializers.menu import MenuSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["menu"])
class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filterset_fields.pop("qr_code")
