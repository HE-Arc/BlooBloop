from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from bloobloopapp import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatRoomConsumer.as_asgi()),
    # re_path(r"ws/chat/(\w+)/$", consumers.ChatRoomConsumer.as_asgi()),
    # re_path(r"ws/chat/$", consumers.ChatRoomConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)
