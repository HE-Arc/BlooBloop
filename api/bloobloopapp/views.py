from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout

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
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid username and/or password.'}, status=status.HTTP_400_BAD_REQUEST)