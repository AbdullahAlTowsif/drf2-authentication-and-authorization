from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size = 2 # every page contains 2 elements
    page_query_param = 'pg' # you can name the page such as pg
    
    # you can modify the elements as how much elements you want to see per page
    page_size_query_param = 'size'

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 2

class ProductCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'price'