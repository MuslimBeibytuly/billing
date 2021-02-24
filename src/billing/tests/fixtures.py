from django.test import Client
from pytest import fixture
from rest_framework.authtoken.models import Token

from billing.models import ProxyUser

data = {
    'username': 'username', 'password': 'password',
}


@fixture
def authenticated_client(client: Client) -> Client:
    user = ProxyUser.objects.create_user(**data)
    token, _ = Token.objects.get_or_create(user=user)
    headers = {
        'HTTP_AUTHORIZATION': f'Token {token.key}',
    }
    client.defaults.update(**headers)
    return client
