from django.db.models import CASCADE, ForeignKey

from apps.app.models.base import BaseModel
from apps.app.models.menu import Menu


class Category(BaseModel):
    menu = ForeignKey(Menu, on_delete=CASCADE, related_name="categories")

    class Meta:
        unique_together = ("menu", "name")
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name} - {self.menu.name}"
