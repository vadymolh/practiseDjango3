# -*- codding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.defaults import page_not_found
from django.http import Http404
from .models import Post, PostCategory

# Create your views here.
def main_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('published_date')
        categories = PostCategory.objects.all()
    else: posts = ""
    context = {
        'posts': posts,
        'sidebar': categories
    }
    return render(request, 'main_page.html', context)

def single_slug(request, single_slug):
    posts_slug = [ p.post_slug for p in Post.objects.all()]
    if single_slug in posts_slug:
        post = Post.objects.get(post_slug=single_slug)
        context = {"post": post}
        return render(request, 'post_view.html', context)
    else:
        raise Http404
        #page_not_found(request, 'Article not found!')




def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Sucsess IN REGISTER!!!")
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Створено новий акаунт: {username}")
            login(request, user)
            return redirect("/")
        else:
            print("ERRORS IN REGISTER!!!")
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]} ")
            return render(request, 'register.html', context={'form': form})
    form = UserCreationForm
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_request(request):
    logout(request)
    return redirect("/")

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "login.html", context)
