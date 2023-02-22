from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MessageItem(models.Model):
    user = models.ForeignKey(
        User, related_name="message_items", on_delete=models.SET_NULL
    )
    conversation = models.ForeignKey(
        Conversation, related_name="message_items", on_delete=models.CASCADE
    )
    content = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
