from django.contrib import admin
from .models import Doctor
from .models import Patient
from .models import Appointment
from .models import News

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(News)
