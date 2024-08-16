from django.http import JsonResponse
from rest_framework import status


def handler404(request, exception=None):
    return JsonResponse(
        data={
            "detail": "Not Found",
        },
        status=status.HTTP_404_NOT_FOUND,
    )


def handler500(request, exception=None):
    return JsonResponse(
        data={
            "detail": "Internal Server Error",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
