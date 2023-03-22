from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "conversation-items", views.ConversationItemViewSet, basename="conversationitem"
)

router.register("message-items", views.MessageItemViewSet, basename="messageitem")
router.register("profile-items", views.ProfileItemViewSet, basename="profileitem")
router.register("users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
