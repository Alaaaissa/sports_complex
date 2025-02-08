from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .models import Staff, Client, Facility, Reservation, Payment
from .serializers import StaffSerializer, ClientSerializer, FacilitySerializer, ReservationSerializer, PaymentSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model



User = get_user_model()

@api_view(['POST'])
def login(request):  # Function name should be 'login'
    email = request.data.get('email')
    phone = request.data.get('phone')

    user = User.objects.filter(email=email).first()
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id, 'email': user.email}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer