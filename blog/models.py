from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='blog/static/img')
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title + ' ' + str(self.created_date)
