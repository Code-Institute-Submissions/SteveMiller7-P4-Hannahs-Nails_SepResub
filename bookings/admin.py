from django.contrib import admin
from .models import Photo, Appointments, Technician

admin.site.register(Photo)

# admin.ModelAdmin is a built in django class
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone')
#     search_fields = ['name']

# @admin.register(Schedule)
# class SchedulerAdmin(admin.ModelAdmin):
#     list_display = ('date_of', 'slot', 'owner')

@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['nail_tech', 'date', 'timeslot', 'customer_name', 'phone_number']
    list_filter = ['nail_tech', ]
    search_fields = ['customer_name',]

# admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(Technician)
