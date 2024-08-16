from django.contrib.auth.models import User
from django.db.models import EmailField, ManyToManyField, TextField, URLField
from phonenumber_field.modelfields import PhoneNumberField

from apps.app.models.base import BaseModel


class Restaurant(BaseModel):
    address = TextField(blank=True, default="")
    phone = PhoneNumberField(blank=True, default="")
    email = EmailField(blank=True, default="")
    website = URLField(blank=True, default="")
    moderators = ManyToManyField(User, related_name="restaurants")

    def __str__(self):
        return self.name
