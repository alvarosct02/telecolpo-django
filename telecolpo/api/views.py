from django.http import JsonResponse
from django.shortcuts import render
from .models import Study
from .serializers import StudySerializer


def studyList(request):

    if request.method == 'GET':
        studies = Study.objects.all()
        serializer = StudySerializer(studies, many=True)
        return JsonResponse(serializer.data, safe=False)
