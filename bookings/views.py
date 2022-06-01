from django.shortcuts import render, redirect
from django.views import generic
from .models import Technician, Photo
from .forms import SchedulePage


class TechnicianList(generic.ListView):
    model = Technician
    template_name = 'appointment_bookings.html'
    paginate_by = 6
    # paginate_by wont be used as there will not be more than 6 technicians. This for my reference only


def Index(request):
    # The View function for index/home page of site
    template_name = "index.html"
    context = {}
    return render(request, 'index.html', context=context)

class Inspiration(generic.ListView):
    # The View function for inspiration page page of site
    model = Photo
    template_name = 'inspiration.html'


def NewBooking(request):
    if request.method == 'POST':
        form = SchedulePage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SchedulePage()
    return render(
        request,
        'appointment_bookings.html',
        {
            'form': SchedulePage(),
        },
    )