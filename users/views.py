from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# API用ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def user_list(request):
    users = User.objects.all()  # 全てのユーザーを取得
    return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)  # ユーザーIDで特定のユーザーを取得
    return render(request, 'users/user_detail.html', {'user': user})
