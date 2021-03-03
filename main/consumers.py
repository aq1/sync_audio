from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SyncAudioConsumer(AsyncJsonWebsocketConsumer):
    """
    This chat consumer handles websocket connections for chat clients.

    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    ##### WebSocket event handlers

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        await self.channel_layer.group_add(
            'all',
            self.channel_name,
        )
        await self.accept()

        # Store which rooms the user has joined on this connection
        # self.rooms = set()

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on
        content['type'] = 'audio.control'
        await self.channel_layer.group_send('all', content)

    async def audio_control(self, event):
        await self.send_json(
            {
                'clientId': event['clientId'],
                'isPlaying': event['isPlaying'],
                'position': event['position'],
            },
        )
