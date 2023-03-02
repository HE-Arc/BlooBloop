from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConversationItem, MessageItem


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
            "url",
            "id",
            "username",
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
