from . import views 
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('inspiration/', views.Inspiration.as_view(), name='photos'),
    # path('appointment_bookings/', views.NewBooking, name="appointment_bookings"),
    path('appointment_bookings/', views.new_appointment, name="appointment_bookings"),
        # Blank path indicates its the default (home page)
    path('my_appointments/', views.BookingList, name="my_appoints"),
    path('edit/<booking_id>', views.EditBooking, name="edit"),
    path('delete/<booking_id>', views.DeleteBooking, name="delete"),
]