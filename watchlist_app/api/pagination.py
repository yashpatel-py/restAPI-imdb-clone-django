from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 1000

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 5
    limit_query_param = "limit"
    offset_query_param = "start"

class WatchListCPagination(CursorPagination):
    page_size = 3