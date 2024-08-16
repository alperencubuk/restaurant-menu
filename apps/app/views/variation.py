from drf_spectacular.utils import extend_schema

from apps.app.models.variation import Variation
from apps.app.serializers.variation import VariationSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["variation"])
class VariationViewSet(BaseModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
