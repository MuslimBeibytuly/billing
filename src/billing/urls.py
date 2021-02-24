from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PaymentViewSet, TransferViewSet

router = DefaultRouter()
router.register(
    prefix='users', viewset=UserViewSet, basename='users',
)
router.register(
    prefix='payments', viewset=PaymentViewSet, basename='payments',
)
router.register(
    prefix='transfers', viewset=TransferViewSet, basename='transfers',
)
urlpatterns = router.urls
