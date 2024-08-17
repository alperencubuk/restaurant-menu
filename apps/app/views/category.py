from drf_spectacular.utils import extend_schema

from apps.app.models.category import Category
from apps.app.serializers.category import CategorySerializer
from apps.app.views.base import BaseModelViewSet


@extend_schema(tags=["category"])
class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all().prefetch_related("sections")
    serializer_class = CategorySerializer
