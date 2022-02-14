from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img', 'text', 'post_slug')

class AddComment(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control','rows': 4, 'cols': 50, 
               'placeholder':'Comment here...'}
    ))
    class Meta:
        model = Comment
        fields = ['content']