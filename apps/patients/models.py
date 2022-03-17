from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Event_type(models.Model):
    """
    Event_type is like a category model for patient,
    datebase relationship is one to many
    """
    type_name = models.CharField(max_length=40,unique=True)

    class Meta:
        verbose_name = "event_type"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name

# this model to save patient information
class Patient(models.Model):
    """
   Patient and  Event_type models are parent models
   Event model is a child model
    """
    patient_id = models.AutoField(unique=True, primary_key=True)  # patient identification
    patient_name = models.CharField(max_length=30, unique=True, verbose_name='patient_name')

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = verbose_name
        ordering = ['-patient_id']

    def __str__(self):
        return self.patient_name


class Event(models.Model):
    """
   Event is a child model of Patient and Event_type
    """
    event_id = models.AutoField(unique=True, primary_key=True)
    event_type = models.ForeignKey(Event_type, null=True, blank=True,on_delete=models.CASCADE,
                                   verbose_name='event type',default="",to_field='type_name'
                                   )
    event_value = models.PositiveIntegerField(default=0, verbose_name='even value', blank=True)
    event_unit = models.CharField(max_length=100, blank=True,
                                  verbose_name='event unit')
    event_time = models.DateTimeField(auto_now=False, verbose_name='event time')
    patient = models.ForeignKey(verbose_name='patient',related_name='events' ,to='Patient', to_field='patient_id', on_delete=models.CASCADE,default="")

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = verbose_name
        ordering = ['-event_id']

    def __str__(self):
        return self.event_type.type_name
