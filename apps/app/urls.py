from django.urls import include, path

from apps.app.views.category import CategoryViewSet
from apps.app.views.item import ItemViewSet
from apps.app.views.menu import MenuViewSet
from apps.app.views.restaurant import RestaurantViewSet
from apps.app.views.section import SectionViewSet
from apps.app.views.variation import VariationViewSet
from config.core import Router

router = Router()

router.register(r"categories", CategoryViewSet)
router.register(r"items", ItemViewSet)
router.register(r"menus", MenuViewSet)
router.register(r"restaurants", RestaurantViewSet)
router.register(r"sections", SectionViewSet)
router.register(r"variations", VariationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
