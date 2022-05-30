from . import views 
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('appointment_bookings/', views.TechnicianList.as_view(), name="appointment_bookings")
    # Blank path indicates its the default (home page)

]