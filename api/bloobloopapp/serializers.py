from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConversationItem, MessageItem, ProfileItem


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    CONVERSATION Serializer                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class ConversationItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConversationItem
        fields = [
            "url",
            "id",
            "name",
        ]


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

    class Meta:
        model = ProfileItem
        fields = [
            "url",
            "id",
            "user",
        ]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                       MESSAGE Serializer                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class MessageItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageItem
        fields = [
            "url",
            "id",
            "content",
        ]
