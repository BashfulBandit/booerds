from django.contrib import admin

from .models import (
    Customer,
    Vendor,
)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vendor)
