from drf_spectacular.utils import extend_schema

from apps.app.models.section import Section
from apps.app.serializers.section import SectionSerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["section"])
class SectionViewSet(BaseModelViewSet):
    queryset = Section.objects.all().prefetch_related("items")
    serializer_class = SectionSerializer
