from django.contrib import admin
from .models import Technician, Customer, Photo

admin.site.register(Photo)
admin.site.register(Technician)

# admin.ModelAdmin is a built in django class
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name']
