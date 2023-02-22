from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import MessageItem
from .serializers import MessageItemSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

# Create your views here.
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
