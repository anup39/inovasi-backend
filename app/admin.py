from django.contrib import admin
from .models import Facility, Refinery, Mill

# Register your models here.
admin.site.register(Facility)
admin.site.register(Refinery)
admin.site.register(Mill)
