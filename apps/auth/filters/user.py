from django.contrib.auth.models import User
from django_filters.rest_framework import FilterSet


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            "id": ["exact"],
            "username": ["exact", "icontains", "istartswith"],
            "email": ["exact", "icontains", "istartswith"],
            "first_name": ["exact", "icontains", "istartswith"],
            "last_name": ["exact", "icontains", "istartswith"],
            "is_active": ["exact"],
            "is_staff": ["exact"],
            "is_superuser": ["exact"],
            "date_joined": ["exact", "gt", "lt", "gte", "lte"],
            "last_login": ["exact", "gt", "lt", "gte", "lte"],
            "restaurants": ["exact"],
            "restaurants__name": ["exact", "icontains", "istartswith"],
        }
