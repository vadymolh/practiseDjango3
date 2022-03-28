from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,
                             help_text="Обов'язкове поле")
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')
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

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'class':'form-control'}
                                ))
    email = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'class':'form-control'}
                                ))
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField( widget = forms.FileInput(attrs={'class':'form-control-file'}))
    about = forms.CharField( widget = forms.Textarea(attrs={'class':'form-control', 'rows': 4}))

    class Meta:
        model = Profile
        fields = ['avatar', 'about']