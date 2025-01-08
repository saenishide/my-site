from django.urls import path
from game_area import views

app_name = 'game_area'
urlpatterns = [
    path('', views.display_top, name='top'),
    path('select_zero_or_one/', views.select_zero_or_one, name='select_zero_or_one'),
    path('check_number/', views.check_number, name='check_number'),
    path('sort_get_list/', views.sort_get_list, name='sort_get_list'),
]