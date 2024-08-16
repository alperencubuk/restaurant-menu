from django.db.models import CASCADE, DecimalField, ForeignKey

from apps.app.models.base import BaseModel
from apps.app.models.item import Item


class Variation(BaseModel):
    item = ForeignKey(Item, on_delete=CASCADE, related_name="variations")
    price = DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ("item", "name")

    def __str__(self):
        return f"{self.name} - {self.item.name}"
