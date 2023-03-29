from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConversationItem, MessageItem, ProfileItem

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                        USER Serializer                        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


class ProfileItemSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)
    conversations = serializers.HyperlinkedRelatedField(
        many=True, view_name="conversationitem-detail", read_only=True
    )
    messages = serializers.HyperlinkedRelatedField(
        many=True, view_name="messageitem-detail", read_only=True
    )

    class Meta:
        model = ProfileItem
        fields = [
            "url",
            "id",
            "user",
            "conversations",
            "messages",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        profile = ProfileItem.objects.create(user=user, **validated_data)
        return profile


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    CONVERSATION Serializer                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class ConversationItemSerializer(serializers.HyperlinkedModelSerializer):
    users = ProfileItemSerializer(many=True, read_only=True)
    messages = serializers.HyperlinkedRelatedField(
        many=True, view_name="messageitem-detail", read_only=True
    )

    class Meta:
        model = ConversationItem
        fields = [
            "url",
            "id",
            "name",
            "users",
            "messages",
        ]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                       MESSAGE Serializer                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class MessageItemSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileItemSerializer(read_only=True)
    conversation = ConversationItemSerializer(read_only=True)

    class Meta:
        model = MessageItem
        fields = [
            "url",
            "id",
            "content",
            "profile",
            "conversation",
        ]
