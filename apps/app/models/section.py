from django.db.models import CASCADE, ForeignKey

from apps.app.models.base import BaseModel
from apps.app.models.category import Category


class Section(BaseModel):
    category = ForeignKey(Category, on_delete=CASCADE, related_name="sections")

    class Meta:
        unique_together = ("category", "name")

    def __str__(self):
        return f"{self.name} - {self.category.name}"
