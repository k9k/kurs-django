from django.contrib import admin
from .models import Rental
# Register your models here.

class RentalAdmin(admin.ModelAdmin):
    ordering = ['who']


admin.site.register(Rental, RentalAdmin)