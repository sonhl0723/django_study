from django.urls import path
from . import views

app_name = 'tft'

urlpatterns = [
    path('', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('search_result/', views.search_result, name='search_result'),
]