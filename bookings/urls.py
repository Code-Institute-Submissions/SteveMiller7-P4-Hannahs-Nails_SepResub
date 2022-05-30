from . import views 
from django.urls import path


urlpatterns = [
    path ('', views.TechnicianList.as_view(), name="home")
    # Blank path indicates its the default (home page)

]