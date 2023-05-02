from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.hashers import make_password

from .models import ConversationItem, MessageItem, ProfileItem
from .serializers import (
    ConversationItemSerializer,
    MessageItemSerializer,
    ProfileItemSerializer,
)


class ConversationItemViewSet(viewsets.ModelViewSet):
    queryset = ConversationItem.objects.all()
    serializer_class = ConversationItemSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="custom-post")
    def custom_conversation(self, request):
        # Retrieve profiles from request
        profile_ids = request.data["users"]
        profiles = []

        for id in profile_ids:
            profiles.append(ProfileItem.objects.get(id=id))

        # Conversation creation
        new_conversation = ConversationItem()
        new_conversation.name = request.data["name"]
        new_conversation.save()

        # add profiles to conversation
        for profile in profiles:
            new_conversation.users.add(profile)

        return Response()

    def partial_update(self, request, *args, **kwargs):
        print("ID:", request.data)
        instance = get_object_or_404(ConversationItem, id=request.data["id"])
        instance.name = request.data["name"]

        instance.users.clear()
        for profile in request.data["users"]:
            instance.users.add(profile["id"])

        instance.save()
        return Response()

    @action(detail=False, methods=["get"], url_path="profile")
    def get_logged_user_conversations(self, request):
        user = get_user(request=request)
        profile = get_object_or_404(ProfileItem, user=user)

        profile_conversations = ConversationItem.objects.filter(users__exact=profile)
        serializer = self.get_serializer(profile_conversations, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MessageItemViewSet(viewsets.ModelViewSet):
    queryset = MessageItem.objects.all()
    serializer_class = MessageItemSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="custom-post")
    def custom_message_create(self, request):
        content = request.data["content"].strip()
        conversation_id = request.data["conversation_id"]

        user = get_user(request=request)
        profile = get_object_or_404(ProfileItem, user=user)

        conversation = ConversationItem.objects.get(id=conversation_id)

        if not content:
            return Response(data="Content is empty", status=status.HTTP_204_NO_CONTENT)

        # Message creation
        new_message = MessageItem()
        new_message.content = content
        new_message.profile = profile
        new_message.conversation = conversation

        new_message.save()

        return Response(status=status.HTTP_201_CREATED)


class ProfileItemViewSet(viewsets.ModelViewSet):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer

    @action(detail=False, methods=["post"])
    def register(self, request):
        username = request.data["username"].strip()
        email = request.data["email"].strip()
        password = request.data["password"].strip()

        existingUsers = User.objects.all().filter(username=username)

        if len(existingUsers) > 0:
            return Response(
                {"error": "An user already exists with this username"},
                status=status.HTTP_409_CONFLICT,
            )

        user = User()
        user.username = username
        user.email = email
        user.password = make_password(password=password)
        user.save()

        profile = ProfileItem()
        profile.user = user
        profile.save()

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def login(self, request):
        user = authenticate(
            request=request,
            username=request.data["username"],
            password=request.data["password"],
        )

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid username and/or password."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=False, methods=["GET"], url_path="authenticated")
    def isAuthenticated(self, request):
        if request.user.is_authenticated:
            return Response(True, status=status.HTTP_200_OK)
        else:
            return Response(False, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request):
        logout(request=request)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="logged-user-id")
    def get_logged_profile_id(self, request):
        if request.user is not None:
            user = get_user(request=request)
            profile = get_object_or_404(ProfileItem, user=user)

            if user is not None and profile is not None:
                return Response(data=profile.id, status=status.HTTP_200_OK)

            return Response(
                {"error": "User not defined"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"error": "User not logged in"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=False, methods=["get"], url_path="logged-username")
    def get_logged_username(self, request):
        if request.user is not None:
            user = get_user(request=request)
            profile = get_object_or_404(ProfileItem, user=user)

            if user is not None and profile is not None:
                return Response(data=user.username, status=status.HTTP_200_OK)

            return Response(
                {"error": "User not defined"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"error": "User not logged in"},
            status=status.HTTP_400_BAD_REQUEST,
        )
