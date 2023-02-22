from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MessageItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "id", "username"]


class MessageItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageItem
        fields = [
            "url",
            "id",
            "user",
            "conversation",
            "content",
            "created_at",
            "updated_at",
        ]
