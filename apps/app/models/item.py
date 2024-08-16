from django.db.models import CASCADE, DecimalField, ForeignKey

from apps.app.models.base import BaseModel
from apps.app.models.section import Section


class Item(BaseModel):
    section = ForeignKey(Section, on_delete=CASCADE, related_name="items")
    price = DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ("section", "name")

    def __str__(self):
        return f"{self.name} - {self.section.name}"
