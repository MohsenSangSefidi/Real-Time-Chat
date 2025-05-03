from channels.generic.websocket import WebsocketConsumer
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync

from .models import ChatGroup, GroupMessages
import json


class ChatsConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.chatroom_id = None
        self.chatroom = None
        self.user = None

        super().__init__(*args, **kwargs)

    def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.user = self.scope['user']

        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_id)

        async_to_sync(self.channel_layer.group_add)(self.chatroom_id, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.chatroom_id, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']

        message = GroupMessages.objects.create(
            body=body,
            author=self.user,
            group=self.chatroom,
        )

        event = {
            'type': 'message_handler',
            'message': message,
        }

        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_id, event
        )

    def message_handler(self, event):
        message = event['message']

        context = {
            'message': message,
            'user': self.user
        }

        html = render_to_string('partial_massage.html', context=context)
        self.send(text_data=html)
