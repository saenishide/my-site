from django.urls import path
from my_area import views

app_name = 'my_area'
urlpatterns = [
    path('', views.display_top, name='top'),

    path('create/', views.display_create, name='create'),
    path('confirm/create/', views.confirm_create, name='confirm_create'),
    path('complete/create/', views.create_post, name='complete_create'),

    path('detail/<int:post_id>/', views.display_detail, name='detail'),

    path('edit/<int:post_id>/', views.display_edit, name='edit'),
    path('confirm/edit/<int:post_id>/', views.confirm_edit, name='confirm_edit'),
    path('complete/edit/<int:post_id>/', views.edit_post, name='complete_edit'),

    path('confirm/delete/<int:post_id>/', views.confirm_delete, name='confirm_delete'),
    path('complete/delete/<int:post_id>/', views.delete_post, name='complete_delete'),
]