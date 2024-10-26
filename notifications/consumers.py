import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # ユーザーの接続を受け入れる
        await self.accept()
    
    async def disconnect(self, close_code):
        # 接続切断時の処理
        pass

    # クライアントからメッセージを受け取った時の処理
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # クライアントにメッセージを送り返す
        await self.send(text_data=json.dumps({
            'message': message
        }))
