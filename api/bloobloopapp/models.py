from django.db import models
from django.contrib.auth.models import User


class ProfileItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} | {self.user.email}"


class ConversationItem(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(ProfileItem, related_name="conversation_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.users.count()} members"


class MessageItem(models.Model):
    profile = models.ForeignKey(
        ProfileItem, on_delete=models.SET_NULL, related_name="messages", null=True
    )
    conversation = models.ForeignKey(
        ConversationItem, on_delete=models.CASCADE, related_name="messages"
    )
    content = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.profile.user.username}: {self.content}"
