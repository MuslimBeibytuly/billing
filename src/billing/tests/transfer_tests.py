from decimal import Decimal

from django.test import Client

from billing.models import ProxyUser


def test_transfers_create_201(db, authenticated_client: Client) -> None:
    first_user = ProxyUser.objects.last()
    first_account = first_user.account
    second_user = ProxyUser.objects.create_user(
        username='username_2', password='password_2',
    )
    second_account = second_user.account
    response = authenticated_client.post(
        path='/api/transfers/', data={
            'amount': '200',
            'to_account': second_user.account.pk,
        }, content_type='application/json',
    )
    assert response.status_code == 201
    assert response.json() == {}
    first_account.refresh_from_db()
    assert first_account.balance == Decimal(value='-200')
    second_account.refresh_from_db()
    assert second_account.balance == Decimal(value='200')
