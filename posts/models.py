from django.db import models

from project import settings


class Post(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    liked_by = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)


    # like_count is added in the serializer

    def __str__(self):
        return f'Post {self.id}: {self.content}'
