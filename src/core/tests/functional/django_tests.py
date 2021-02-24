from django.test import Client
from requests import Response


def test_django(db, client: Client) -> None:
    response: Response = client.get(path='')
    assert 404 == response.status_code
