from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Study
from .serializers import StudySerializer


@api_view(['GET', 'POST'])
def study_list(request):
    if request.method == 'GET':
        studies = Study.objects.all()
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['read'] = True
        request.data['status'] = 'Pendiente'
        serializer = StudySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def study_detail(request, pk):
    try:
        study = Study.objects.get(pk=pk)
    except Study.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudySerializer(study)
        return Response(serializer.data)
