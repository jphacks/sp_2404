from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    # ここで related_name を指定して競合を避ける
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # デフォルトの'related_name'と区別する
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # デフォルトの'related_name'と区別する
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    def __str__(self):
        return self.username
