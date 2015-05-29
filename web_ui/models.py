from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Report(models.Model):
    title = models.CharField('Title', max_length=255)
    content = models.TextField('Content', max_length=4096)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.title
