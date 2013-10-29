from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('visible', 'allow_comments', 'user', 'created', 'modified')
