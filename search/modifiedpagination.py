from rest_framework import pagination

#CursorBasePagination on publishedAt with each page giving 7 results
class CursorPaginationWithOrder(pagination.CursorPagination):
    ordering = ['-publishedat','-id']

class PageNumberPagination (pagination.PageNumberPagination):
    page_size = 6