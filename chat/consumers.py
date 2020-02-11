from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from chat.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

    async def connect(self):
        # Join room group
        # other_user = self.scope['url_route']['kwargs']['user_id']
        # room_obj = await self.get_room(other_user)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_from = self.scope['user']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user_from.first_name,
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'user': user,
            'message': message
        }))

    @database_sync_to_async
    def get_room(self, user2):
        return Room.objects.get_or_new(self.scope['user'], user2)[0]

    @database_sync_to_async
    def create_chat_message(self, user, msg):
        return Message.objects.create(author=user, msg=msg)
