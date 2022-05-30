from django.shortcuts import render
from django.views import generic
from .models import Technician


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

def Inspiration(request):
    # The View function for index/home page of site
    template_name = "inspiration.html"
    context = {}
    return render(request, 'inspriation.html', context=context)