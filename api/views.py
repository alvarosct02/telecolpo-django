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
        serializer = StudySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
