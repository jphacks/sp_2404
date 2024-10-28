from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('generate-image/', views.generate_image_view, name='generate_image'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]