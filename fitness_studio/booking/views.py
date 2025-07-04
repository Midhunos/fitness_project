from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from pytz import timezone as tz
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
# Create your views here.
# List all upcoming classes
class ClassListView(APIView):
    def get(self, request):
        user_tz = request.GET.get("timezone", "Asia/Kolkata")
        classes = FitnessClass.objects.filter(start_time__gte=now())
        serializer = FitnessClassSerializer(classes, many=True)
        data = serializer.data
        for item in data:
            utc_time = FitnessClass.objects.get(id=item["id"]).start_time
            item["start_time"] = utc_time.astimezone(tz(user_tz)).strftime('%Y-%m-%d %H:%M:%S %Z')
        return Response(data)

# Book a spot in a class
class BookingCreateView(APIView):
    def post(self, request):
        class_id = request.data.get("class_id")
        name = request.data.get("client_name")
        email = request.data.get("client_email")

        if not all([class_id, name, email]):
            return Response({"error": "All fields are required."}, status=400)

        try:
            fitness_class = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Class not found."}, status=404)

        if fitness_class.available_slots <= 0:
            return Response({"error": "No slots available."}, status=400)

        Booking.objects.create(
            fitness_class=fitness_class,
            client_name=name,
            client_email=email
        )
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({"message": "Booking successful."}, status=201)

# View all bookings by a user
class UserBookingsView(APIView):
    def get(self, request):
        email = request.GET.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=400)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
