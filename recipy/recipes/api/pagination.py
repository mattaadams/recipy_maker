from rest_framework.pagination import PageNumberPagination


class RecipePageNumberPagination(PageNumberPagination):
    page_size = 20


class IngredientPageNumberPagination(PageNumberPagination):
    page_size = 20
