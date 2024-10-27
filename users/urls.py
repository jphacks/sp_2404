# users/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # ユーザー一覧
    # path('<int:user_id>/', views.user_detail, name='user_detail'),  # ユーザー詳細
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
]
