from rest_framework.pagination import PageNumberPagination


class RecipePageNumberPagination(PageNumberPagination):
    page_size = 5


class IngredientPageNumberPagination(PageNumberPagination):
    page_size = 20
