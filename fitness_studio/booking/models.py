from django.db import models


# fitnessclass table
class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()  # Stored in UTC
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} at {self.start_time} by {self.instructor}"
# booking table
class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"

