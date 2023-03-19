from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time info', {'fields': ['year']}),
        ('Car info', {'fields': ['brand']})
    ]

admin.site.register(Car, CarAdmin)