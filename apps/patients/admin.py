from django.contrib import admin

# Register your models here.
from . import models
from .models import Event_type, Patient,Event


class EventAdmin(admin.ModelAdmin):
    search_fields = ['event_id', 'event_type', 'event_value', 'event_unit', 'event_time', 'patient']
    list_filter = ('event_id', 'event_type', 'event_value', 'event_unit', 'event_time', 'patient')


admin.site.register(Event, EventAdmin)


class PatientAdmin(admin.ModelAdmin):
    search_fields = ['patient_id', 'patient_name']
    list_filter = ('patient_id', 'patient_name')


admin.site.register(Patient, PatientAdmin)


class EventypeAdmin(admin.ModelAdmin):
    search_fields = ['type_name',]
    list_filter = ('type_name', )


admin.site.register(Event_type, EventypeAdmin)