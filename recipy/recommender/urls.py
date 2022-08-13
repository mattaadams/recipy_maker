from django.urls import path, include
from .views import RecommenderListView


urlpatterns = [path('recommendations/', RecommenderListView.as_view(), name='recipe-recommendations')]
