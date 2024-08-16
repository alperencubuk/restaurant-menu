import base64
import logging
from io import BytesIO

from drf_spectacular.utils import extend_schema
from qrcode.main import QRCode
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.qr.serializers.qrcode import QRCodeGenerateSerializer

logger = logging.getLogger(__name__)


@extend_schema(tags=["qr"])
class QRCodeGenerateViewSet(GenericViewSet):
    serializer_class = QRCodeGenerateSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            qr = QRCode()
            qr.add_data(serializer.validated_data["text"])
            qr.make(fit=True)
            img = qr.make_image(
                fill_color=serializer.validated_data["fill_color"],
                back_color=serializer.validated_data["back_color"],
            )

            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            return Response(data={"qr_code_base64": img_str}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.exception(f"Failed to generate QR code. Error: {e}")
            return Response(
                data={"detail": "An error occurred while generating QR code"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
