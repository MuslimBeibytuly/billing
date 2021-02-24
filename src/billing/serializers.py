from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Payment, ProxyUser, Transfer, Account


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, write_only=True, min_length=8, validators=(
            UniqueValidator(queryset=User.objects.all()),
        ),
    )
    password = serializers.CharField(
        required=True, write_only=True, min_length=8,
    )
    token = serializers.CharField(read_only=True, source='auth_token.key')

    class Meta:
        model = ProxyUser
        fields = ('username', 'password', 'token',)

    def create(self, validated_data):
        user = ProxyUser.objects.create_user(**validated_data)
        return user


class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    amount = serializers.DecimalField(
        write_only=True, max_digits=24, decimal_places=8,
    )

    class Meta:
        model = Payment
        fields = ('user', 'amount',)


class TransferSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    amount = serializers.DecimalField(
        write_only=True, max_digits=24, decimal_places=8,
    )
    to_account = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Account.objects.all(),
    )

    class Meta:
        model = Transfer
        fields = ('user', 'amount', 'to_account',)
