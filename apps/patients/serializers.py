from rest_framework import serializers
from .models import Event_type, Patient, Event
from django.db.models import Avg, Max, Min, Count


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1


class Event_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_type
        fields = "__all__"
        depth = 1


class PatientSerializer(serializers.ModelSerializer):
    # coustomize serializers field add event_type and event_aggregation to PatientSerializer

    type1 = serializers.SerializerMethodField('_get_event_HR')
    type2 = serializers.SerializerMethodField('_get_event_RR')


    HR_aggregation = serializers.SerializerMethodField('_get_aggregatio_hr')
    RR_aggregation = serializers.SerializerMethodField('_get_aggregatio_rr')


    # add event_type field
    def _get_event_HR(self, patient_object):
        HR = 'HR'
        return HR

    # add event_type field
    def _get_event_RR(self, patient_object):
        RR = 'RR'
        return RR

    # add _get_aggregatio field
    def _get_aggregatio_hr(self, patient_object):
        HR_aggregation = Event.objects.filter(patient_id=patient_object.patient_id,event_type='HR') \
            .aggregate(mininum_event_value=Min('event_value'),
                       maximum_event_value=Max('event_value'),
                       average_event_value=Avg('event_value'),
                       count_of_events=Count('event_value'),
                       time_of_earliest_event=Min('event_time'),
                       time_of_oldest_event=Max('event_time'),
                       )

        return HR_aggregation

    # add _get_aggregatio field
    def _get_aggregatio_rr(self, patient_object):
        RR_aggregation = Event.objects.filter(patient_id=patient_object.patient_id,event_type='RR') \
            .aggregate(mininum_event_value=Min('event_value'),
                       maximum_event_value=Max('event_value'),
                       average_event_value=Avg('event_value'),
                       count_of_events=Count('event_value'),
                       time_of_earliest_event=Min('event_time'),
                       time_of_oldest_event=Max('event_time'),
                       )

        return RR_aggregation

    class Meta:
        model = Patient
        fields = ['patient_id','patient_name','type1','HR_aggregation','type2','RR_aggregation']
