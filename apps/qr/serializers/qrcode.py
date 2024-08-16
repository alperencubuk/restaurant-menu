from PIL import ImageColor
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class QRCodeGenerateSerializer(Serializer):
    text = CharField(write_only=True)
    fill_color = CharField(default="black", write_only=True)
    back_color = CharField(default="white", write_only=True)
    qr_code_base64 = CharField(read_only=True)

    def validate_fill_color(self, value):
        return self._validate_color(value)

    def validate_back_color(self, value):
        return self._validate_color(value)

    @staticmethod
    def _validate_color(value):
        try:
            ImageColor.getrgb(value)
        except ValueError:
            raise ValidationError(f"{value} is not a valid color.")
        return value
