from django.db import models


# Create your models here.
class Study(models.Model):

    identifier = models.CharField(max_length=200)
    initials = models.CharField(max_length=200)
    history_number = models.CharField(max_length=200)

    birthday = models.CharField(max_length=200)
    fur = models.CharField(max_length=200)
    papEnable = models.BooleanField()
    pap = models.CharField(max_length=200)
    ivaa = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    diagram = models.CharField(max_length=200)

    max_tries = models.CharField(max_length=200)
    good_photo = models.BooleanField()
    bad_photo_reasons = models.CharField(max_length=200)

    created_at = models.CharField(max_length=200)
    submitted_at = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    read = models.BooleanField()


