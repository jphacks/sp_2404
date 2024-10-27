from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet, user_list
from posts.views import PostViewSet, post_list
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

def redirect_to_home(request):
    # 任意のURLにリダイレクト（ここでは 'users/' にリダイレクト）
    return redirect('posts/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # APIエンドポイント
    path('api/auth/', include('rest_framework.urls')),  # 認証API
    path('api/allauth/', include('allauth.urls')),  # ソーシャル認証API
    path('users/', include('users.urls')),  # ユーザーのURL
    path('posts/', include('posts.urls')),  # 投稿のURL
    path('', redirect_to_home),  # 空のパスにアクセスした場合のリダイレクト
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)