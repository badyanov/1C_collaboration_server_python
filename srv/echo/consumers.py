from channels.generic.websocket import AsyncWebsocketConsumer

class Echo(AsyncWebsocketConsumer):
    async def connect(self):
        return await super().connect()

    async def disconnect(self, code):
        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        return await super().send(text_data)