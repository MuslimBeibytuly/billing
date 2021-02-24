from decimal import Decimal

from django.test import Client

from billing.models import Account


def test_payments_create_201(db, authenticated_client: Client) -> None:
    response = authenticated_client.post(
        path='/api/payments/', data={
            'amount': '200',
        }, content_type='application/json',
    )
    assert response.status_code == 201
    assert response.json() == {}
    account = Account.objects.last()
    assert account.balance == Decimal(value='200')
