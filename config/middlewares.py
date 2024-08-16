import json
import logging
from time import time

from django.conf import settings
from rest_framework import status
from shortuuid import uuid


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        if not self._logging_enabled(request):
            return self.get_response(request)

        start_time = time()
        request_body = self._convert_json(request.body.decode())
        response = self.get_response(request)
        response_body = self._convert_json(response.content.decode())
        run_time = time() - start_time

        log_message = json.dumps(
            obj={
                "request_id": uuid(),
                "method": request.method,
                "path": request.get_full_path(),
                "status_code": response.status_code,
                "request_body": request_body,
                "response_body": response_body,
                "user": str(request.user),
                "run_time": f"{run_time:.3f} seconds",
            },
            indent=4,
        )

        self.logger.log(self._get_log_level(response.status_code), log_message)
        return response

    @staticmethod
    def _convert_json(data):
        try:
            data = json.loads(data)
            if data.get("password"):
                data["password"] = "******"
            return data
        except Exception:
            return data

    @staticmethod
    def _get_log_level(status_code):
        if status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR:
            return logging.ERROR
        if status_code >= status.HTTP_400_BAD_REQUEST:
            return logging.WARNING
        return logging.INFO

    @staticmethod
    def _logging_enabled(request):
        if not settings.REQUEST_LOGGING_ENABLED:
            return False

        is_included_path = any(
            request.path.startswith(path) if path else False
            for path in settings.REQUEST_LOGGING_INCLUDE_PATHS
        )
        is_excluded_path = any(
            request.path.startswith(path) if path else False
            for path in settings.REQUEST_LOGGING_EXCLUDE_PATHS
        )
        return is_included_path and not is_excluded_path
