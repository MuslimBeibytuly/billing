from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Payment, Transfer
from .serializers import UserSerializer, PaymentSerializer, TransferSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('post',)

    @action(detail=False, methods=('post',))
    def obtain_token(self, request, *args, **kwargs):
        self.serializer_class = AuthTokenSerializer
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ('post',)
    permission_classes = (IsAuthenticated,)


class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    http_method_names = ('post',)
    permission_classes = (IsAuthenticated,)
