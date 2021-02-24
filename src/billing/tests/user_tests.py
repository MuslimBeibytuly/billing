from django.contrib.auth.models import User
from django.test import Client
from rest_framework.authtoken.models import Token

from .fixtures import data


def test_users_create_201(db, client: Client) -> None:
    response = client.post(
        path='/api/users/', data=data, content_type='application/json',
    )
    assert response.status_code == 201
    token = Token.objects.last()
    assert response.json() == {'token': token.key}


def test_users_obtain_token_200(db, client: Client) -> None:
    User.objects.create_user(**data)
    response = client.post(
        path='/api/users/obtain_token/',
        data=data, content_type='application/json',
    )
    assert response.status_code == 200
    token = Token.objects.last()
    assert response.json() == {'token': token.key}
