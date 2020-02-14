from var_dump import var_dump
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from chat.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.other_user = self.scope['url_route']['kwargs']['id']

    async def websocket_connect(self, message):
        self.room = await self.get_room()
        self.room_group_name = f'chat_{self.room.id}'

        # Join room group
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
        message = text_data_json.get('message', None)
        if message is not None:
            user_from = self.scope['user']

            await self.create_chat_message(message)

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
    def get_room(self):
        return Room.objects.get_or_new(
            self.scope['user'],
            self.scope['url_route']['kwargs']['id']
        )[0]

    @database_sync_to_async
    def create_chat_message(self, msg):
        return Message.objects.create(
            room=self.room,
            author=self.scope['user'],
            message=msg
        )
