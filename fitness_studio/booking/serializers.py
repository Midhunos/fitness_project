from rest_framework import serializers
from .models import FitnessClass, Booking


# fitness class serializer
class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

# bokking serializers
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = '__all__'
        read_only_fields = ['booked_at']