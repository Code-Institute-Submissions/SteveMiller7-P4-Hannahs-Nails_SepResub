from django.contrib import admin
from .models import Technician, Customer, Photo, Scheduler

admin.site.register(Photo)
admin.site.register(Technician)

# admin.ModelAdmin is a built in django class
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name']

@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'slot')
