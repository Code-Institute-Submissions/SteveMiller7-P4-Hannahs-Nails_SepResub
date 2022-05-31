from django.shortcuts import render
from django.views import generic
from .models import Technician, Photo


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
