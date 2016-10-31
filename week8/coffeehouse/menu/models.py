from django.db import models


class Special(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
