from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, ClientViewSet, FacilityViewSet, ReservationViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]