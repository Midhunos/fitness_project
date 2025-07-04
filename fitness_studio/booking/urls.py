from django.urls import path
from .views import ClassListView, BookingCreateView, UserBookingsView

urlpatterns = [
    path("api/classes/", ClassListView.as_view(),name="clasess"),
    path("api/book/", BookingCreateView.as_view(),name="booking"),
    path("api/bookings/", UserBookingsView.as_view(),name="bookings"),
]