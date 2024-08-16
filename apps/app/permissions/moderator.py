from rest_framework.permissions import BasePermission

from apps.app.models.category import Category
from apps.app.models.item import Item
from apps.app.models.menu import Menu
from apps.app.models.restaurant import Restaurant
from apps.app.models.section import Section
from apps.app.models.variation import Variation


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if restaurant := self._get_restaurant_from_request(request):
            return self._is_moderator(request.user, restaurant)
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if restaurant := self._get_restaurant_from_obj(obj):
            return self._is_moderator(request.user, restaurant)
        return False

    @staticmethod
    def _is_moderator(user, restaurant):
        if user.id in restaurant.moderators.values_list("id", flat=True):
            return True
        return False

    @staticmethod
    def _get_restaurant_from_obj(obj):
        relations = {
            Restaurant: lambda x: x,
            Menu: lambda x: x.restaurant,
            Category: lambda x: x.menu.restaurant,
            Section: lambda x: x.category.menu.restaurant,
            Item: lambda x: x.section.category.menu.restaurant,
            Variation: lambda x: x.item.section.category.menu.restaurant,
            "default": lambda x: None,
        }

        return relations.get(type(obj), "default")(obj)

    @staticmethod
    def _get_restaurant_from_request(request):
        relations = {
            "restaurant_id": lambda x: Restaurant.objects.filter(id=x).first(),
            "menu_id": lambda x: Menu.objects.filter(id=x)
            .select_related("restaurant")
            .first()
            .restaurant,
            "category_id": lambda x: Category.objects.filter(id=x)
            .select_related("menu__restaurant")
            .first()
            .menu.restaurant,
            "section_id": lambda x: Section.objects.filter(id=x)
            .select_related("category__menu__restaurant")
            .first()
            .category.menu.restaurant,
            "item_id": lambda x: Item.objects.filter(id=x)
            .select_related("section__category__menu__restaurant")
            .first()
            .section.category.menu.restaurant,
            "variation_id": lambda x: Variation.objects.filter(id=x)
            .select_related("item__section__category__menu__restaurant")
            .first()
            .item.section.category.menu.restaurant,
        }

        data = request.data
        for field, get_restaurant in relations.items():
            if field in data:
                try:
                    return get_restaurant(data[field])
                except AttributeError:
                    return None
        return None
