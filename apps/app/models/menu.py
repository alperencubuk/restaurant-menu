from django.db.models import CASCADE, ForeignKey, TextField

from apps.app.models.base import BaseModel
from apps.app.models.restaurant import Restaurant


class Menu(BaseModel):
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE, related_name="menus")
    qr_code = TextField(blank=True, default="")

    class Meta:
        unique_together = ("restaurant", "name")

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
