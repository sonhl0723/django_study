from django.urls import path
from . import views

app_name = 'tft'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('search_result/', views.search_result, name='search_result'),
]