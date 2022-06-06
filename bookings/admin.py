from django.contrib import admin
from .models import Customer, Photo, Schedule

admin.site.register(Photo)

# admin.ModelAdmin is a built in django class
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name']

@admin.register(Schedule)
class SchedulerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'slot')
