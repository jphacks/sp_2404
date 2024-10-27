from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'location', 'image', 'tags', 'is_virtual']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'ここに投稿の内容を入力してください', 'rows': 5}),
            'location': forms.TextInput(attrs={'placeholder': 'ロケーションを入力（任意）'}),
        }

class ImageGenerationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'ここに投稿の内容を入力してください', 'rows': 5}),
            'location': forms.TextInput(attrs={'placeholder': 'ロケーションを入力（任意）'}),
        }