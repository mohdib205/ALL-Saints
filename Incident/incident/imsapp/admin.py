from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(IncidentTicket)
admin.site.register(IncidentType)
admin.site.register(ContributingFactor)
