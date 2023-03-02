from django.db import models
from django.contrib.auth.models import User


class ConversationItem(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfileItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    conversations = models.ManyToManyField(ConversationItem, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MessageItem(models.Model):
    # user = models.ForeignKey(
    #     User, related_name="message_items", on_delete=models.SET_NULL, null=True
    # )
    # conversation = models.ForeignKey(
    #     ConversationItem, related_name="message_items", on_delete=models.CASCADE
    # )
    content = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
