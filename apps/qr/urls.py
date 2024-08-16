from django.urls import include, path

from apps.qr.views.qrcode import QRCodeGenerateViewSet
from config.core import Router

router = Router()

router.register(r"generate", QRCodeGenerateViewSet, basename="generate-qr")

urlpatterns = [
    path("", include(router.urls)),
]
