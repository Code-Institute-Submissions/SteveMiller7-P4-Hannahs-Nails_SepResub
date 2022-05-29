from django.contrib import admin
from .models import Technician, Customer

admin.site.register(Technician)

# admin.ModelAdmin is a built it django class
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name']
