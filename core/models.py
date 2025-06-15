from django.db import models
from django.contrib.auth.models import User

class Taskgroup(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    group = models.ForeignKey(Taskgroup, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email_reminder_sent = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    executor = models.CharField(max_length=255)

