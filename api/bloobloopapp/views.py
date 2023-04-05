from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, get_user, login, logout

from .models import ConversationItem, MessageItem, ProfileItem
from .serializers import (
    ConversationItemSerializer,
    MessageItemSerializer,
    ProfileItemSerializer,
    UserSerializer,
)


class ConversationItemViewSet(viewsets.ModelViewSet):
    queryset = ConversationItem.objects.all()
    serializer_class = ConversationItemSerializer

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


class MessageItemViewSet(viewsets.ModelViewSet):
    queryset = MessageItem.objects.all()
    serializer_class = MessageItemSerializer

    # The following method hasn't been tested
    @action(detail=True, methods=["GET"], url_path="recent-messages")
    def recent_messages(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        recent_messages = MessageItem.objects.filter(user=user).order_by("created_at")
        serializer = self.get_serializer(recent_messages)
        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileItemViewSet(viewsets.ModelViewSet):
    queryset = ProfileItem.objects.all()
    serializer_class = ProfileItemSerializer

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

    @action(detail=False, methods=["get"], url_path="authenticated")
    def isAuthentificated(self, request):
        if request.user.is_authenticated:
            return Response(True, status=status.HTTP_200_OK)
        else:
            return Response(False, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request):
        logout(request=request)
        print("Logged out")
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="logged-user-id")
    def get_logged_user_id(self, request):
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
