from rest_framework.pagination import PageNumberPagination
from rest_framework.routers import DefaultRouter


class Router(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = "/?"


class Pagination(PageNumberPagination):
    page_size = None
    page_size_query_param = "page_size"
    max_page_size = 1000
