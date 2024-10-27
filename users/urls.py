# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # ユーザー一覧
    path('<int:user_id>/', views.user_detail, name='user_detail'),  # ユーザー詳細
]
