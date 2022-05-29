from django.shortcuts import render
from django.views import generic
from .models import Technician


class TechnicianList(generic.ListView):
    model = Technician
    template_name = 'index.html'
    paginate_by = 6
    # paginate_by wont be used as there will not be more than 6 technicians. This for my reference only
    
