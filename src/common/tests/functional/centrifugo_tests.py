from typing import List, Dict

from common.services import Centrifugo


def test_centrifugo():
    centrifugo = Centrifugo()
    centrifugo.publish(channel='notifications', data={})
    messages: List[Dict, ...] = centrifugo.client.history(
        channel='seed:notifications',
    )
    assert len(messages) == 1
    centrifugo.client.history_remove(channel='seed:notifications')


def test_centrifugo_jwt_token():
    centrifugo = Centrifugo()
    token = centrifugo.jwt_token_for(user_id=123)
    assert len(token) > 64
