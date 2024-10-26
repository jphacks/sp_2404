from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'bio', 'followers_count', 'following_count']
