
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Study


class StringArrayField(serializers.Field):

    def to_representation(self, value):
        return value.split('|')

    def to_internal_value(self, data):
        return '|'.join(data)


class NestedPatientSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    initials = serializers.CharField()
    history_number = serializers.CharField()


class NestedClinicHistorySerializer(serializers.Serializer):
    birthday = serializers.CharField()
    fur = serializers.CharField()
    papEnable = serializers.BooleanField()
    pap = serializers.CharField()
    ivaa = serializers.CharField()
    diagnosis = StringArrayField()
    notes = serializers.CharField()
    diagram = serializers.CharField()


class NestedSurveySerializer(serializers.Serializer):
    max_tries = serializers.CharField()
    good_photo = serializers.BooleanField()
    bad_photo_reasons = StringArrayField()


class StudySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    submitted_at = serializers.DateTimeField()
    status = serializers.CharField(max_length=200)
    read = serializers.CharField(max_length=200)

    patient = NestedPatientSerializer(source='*')
    clinic_history = NestedClinicHistorySerializer(source='*')
    survey = NestedSurveySerializer(source='*')

    class Meta:
        model = Study
        fields = [
            'patient',
            'clinic_history',
            'survey',
            'created_at',
            'submitted_at',
            'status',
            'read',
        ]
