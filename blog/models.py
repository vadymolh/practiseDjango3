# -*- codding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostCategory(models.Model):
    category_name = models.CharField(max_length=80)
    category_info = models.CharField(max_length=280)
    category_slug = models.CharField(max_length=80, default="default")
    class Meta:
        verbose_name_plural = "Категорії"
    def __str__(self):
        return f"{self.category_name} URL: {self.category_slug}"

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='blog/static/img',
        height_field=None,
        width_field=None,
        max_length=100)
    published_date = models.DateTimeField(null=True, blank=True)
    post_slug = models.CharField(max_length=80, default="default_post")
    post_category = models.ForeignKey(PostCategory, default=1, on_delete=models.SET_DEFAULT)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title + ' ' + str(self.created_date)

class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content






