from django.shortcuts import render, redirect
from django.views import generic
from .models import Photo
from .forms import AppointmentForm



def Index(request):
    # The View function for index/home page of site
    template_name = "index.html"
    context = {}
    return render(request, 'index.html', context=context)

class Inspiration(generic.ListView):
    # The View function for inspiration page page of site
    model = Photo
    template_name = 'inspiration.html'


# def NewBooking(request):
#     if request.method == 'POST':
#         form = SchedulePage(request.POST)
#         if form.is_valid():
#             form.owner = request.user
#             form.save()
#             return redirect('/')
#     else:
#         form = SchedulePage()
#     return render(
#         request,
#         'appointment_bookings.html',
#         {
#             'form': SchedulePage(),
#         },
#     )
def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_bookings.html')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_bookings.html', {'form': form})