from rest_framework import pagination


class DoctorsListPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50
    page_query_param = 'page'
