import os
import django
from datetime import datetime, timedelta
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitness_studio.settings")
django.setup()

from booking.models import FitnessClass

FitnessClass.objects.all().delete()

now = datetime.now(pytz.UTC)
classes = [
    ("Yoga", "Anjali", now + timedelta(days=1, hours=6)),
    ("Zumba", "Rahul", now + timedelta(days=2, hours=7)),
    ("HIIT", "Nina", now + timedelta(days=3, hours=5)),
]

for name, instructor, time in classes:
    FitnessClass.objects.create(
        name=name,
        instructor=instructor,
        start_time=time,
        available_slots=5
    )

print("Seed data added.")
