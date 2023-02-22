from django.db import models
from django.contrib.auth.models import User


class ConversationItem(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
