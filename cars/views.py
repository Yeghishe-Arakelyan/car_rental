from rest_framework import generics
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsReservationOwnerOrStaff
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]

class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer 
    permission_classes = [IsAdminUser]

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]  
    def perform_create(self, serializer):
        customer_instance = self.request.user
        serializer.save(customer=customer_instance)

class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminUser | IsReservationOwnerOrStaff]

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsReservationOwnerOrStaff]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Assuming 'start_date' and 'end_date' are DateField or DateTimeField
        start_date = instance.start_date
        end_date = instance.end_date

        # Calculate the rental duration in days
        rental_duration = (end_date - start_date).days

        # Retrieve the daily rental price from the associated car
        car_daily_price = instance.car.price_per_day

        # Calculate the total rental cost
        total_cost = rental_duration * car_daily_price

        # Add the total cost to the serializer's data
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['total_cost'] = total_cost

        return Response(data)


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer