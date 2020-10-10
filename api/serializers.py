
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
    pap = serializers.CharField(required=False, allow_blank=True)
    ivaa = serializers.CharField()
    diagnosis = StringArrayField()
    notes = serializers.CharField()
    diagram = serializers.CharField(required=False, allow_blank=True)


class NestedSurveySerializer(serializers.Serializer):
    max_tries = serializers.CharField()
    good_photo = serializers.BooleanField()
    bad_photo_reasons = StringArrayField()


class StudySerializer(serializers.ModelSerializer):
    created_at = serializers.CharField()
    submitted_at = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(max_length=200, required=False, allow_blank=True)
    read = True
    id = serializers.IntegerField(read_only=True, required=False, allow_null=True)

    patient = NestedPatientSerializer(source='*')
    clinic_history = NestedClinicHistorySerializer(source='*')
    survey = NestedSurveySerializer(source='*')

    class Meta:
        model = Study
        fields = [
            'id',
            'patient',
            'clinic_history',
            'survey',
            'created_at',
            'submitted_at',
            'status',
            'read',
        ]
