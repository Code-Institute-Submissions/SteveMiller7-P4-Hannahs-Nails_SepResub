from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Photo, Appointments
from .forms import AppointmentForm
from django.contrib import messages



def Index(request):
    # The View function for index/home page of site
    template_name = "index.html"
    context = {}
    return render(request, 'index.html', context=context)


class Inspiration(generic.ListView):
    # The View function for inspiration page of site
    model = Photo
    template_name = 'inspiration.html'



def PriceList(request):
    # The View function for index/home page of site
    template_name = "index.html"
    context = {}
    return render(request, 'prices.html', context=context)


def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            # The above line automatically adds the logged in users name to the back end booking when an appointment is made. 
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Your appointment has been made. Thank you.')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Your appointment was not made, Please try again.')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_bookings.html', {'form': form})


def BookingList(request):
    # function bring over booking details from admin site.
    booking_list = Appointments.objects.all().filter(user=request.user).order_by('date')
    return render(request, 'my_appointments.html', {'booking_list': booking_list})


def EditBooking(request, booking_id):
    booking = get_object_or_404(Appointments, id=booking_id)
    form = AppointmentForm(instance=booking)

    # Post handler
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=booking)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            # The above line automatically adds the logged in users name to the back end booking when an appointment is made. 
            obj.save()
            messages.add_message(request, messages.INFO, 'Your appointment has been changed. Thank you.')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Your appointment was not changed, Please try again.')
        
    return render(request, 'edit_booking.html', {'form': form})


def DeleteBooking(request, booking_id):
    booking = get_object_or_404(Appointments, id=booking_id)
    messages.add_message(request, messages.SUCCESS, 'Your appointment has been deleted. Thank you.')
    booking.delete()

    return redirect('/')

