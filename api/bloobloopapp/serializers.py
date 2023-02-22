from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ConversationItem


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


class ComplexUserSerializer(UserSerializer):
    conversations = serializers.HyperlinkedRelatedField(
        many=True, view_name="conversation-detail", read_only=True
    )

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ["conversations"]


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
            "users",
        ]


class ComplexConversationItemSerializer(ConversationItemSerializer):
    users_objects = serializers.HyperlinkedRelatedField(
        many=True, view_name="user_detail", read_only=True
    )

    class Meta:
        model = ConversationItem
        fields = ConversationItemSerializer.Meta.fields + ["users_objects"]
