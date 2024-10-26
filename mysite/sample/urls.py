from django.urls import path
from sample import views

app_name = 'sample'
urlpatterns = [
    path('post/create/', views.create_post, name='create_post'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/', views.read_post, name='read_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]