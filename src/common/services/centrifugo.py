from typing import Dict

from cent import Client
from django.conf import settings
from jwt import encode


class Centrifugo:
    def __init__(self):
        super().__init__()
        self.__url = settings.CENTRIFUGO_URL
        self.__api_key = settings.CENTRIFUGO_API_KEY
        self.__secret = settings.CENTRIFUGO_SECRET
        self.__namespace = settings.CENTRIFUGO_NAMESPACE
        self.client = Client(address=self.__url, api_key=self.__api_key)

    def jwt_token_for(self, user_id: int) -> str:
        return encode(
            payload={'sub': str(user_id)},
            key=self.__secret, algorithm='HS256',
        )

    def publish(self, channel: str, data: Dict) -> None:
        self.client.publish(
            channel=f'{self.__namespace}:{channel}', data=data,
        )
