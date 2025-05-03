from django.urls import path
from .consumers import ChatsConsumer

websocket_urlpatterns = [
    path('ws/chatroom/<chatroom_id>', ChatsConsumer.as_asgi())
]
