from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConversationItem, MessageItem, ProfileItem


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                        USER Serializer                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class ProfileItemSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)
    message_items = serializers.HyperlinkedRelatedField(
        many=True, view_name="messageitem-detail", read_only=True
    )

    class Meta:
        model = ProfileItem
        fields = [
            "url",
            "id",
            "user",
            "conversations",
            "message_items",
        ]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    CONVERSATION Serializer                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class ConversationItemSerializer(serializers.HyperlinkedModelSerializer):
    users = ProfileItemSerializer(many=True, read_only=True)

    class Meta:
        model = ConversationItem
        fields = [
            "url",
            "id",
            "name",
            "users",
        ]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                       MESSAGE Serializer                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class MessageItemSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileItemSerializer(read_only=True)

    class Meta:
        model = MessageItem
        fields = [
            "url",
            "id",
            "content",
            "profile",
        ]
