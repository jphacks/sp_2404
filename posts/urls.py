from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 投稿一覧
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # 投稿詳細
]
