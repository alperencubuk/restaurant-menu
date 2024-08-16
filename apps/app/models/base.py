from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    IntegerField,
    Model,
    TextField,
)


class BaseModel(Model):
    name = CharField(max_length=255)
    image = TextField(blank=True, default="")
    description = TextField(blank=True, default="")
    is_active = BooleanField(default=True, db_index=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    order = IntegerField(
        default=1000,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        db_index=True,
    )

    class Meta:
        abstract = True
