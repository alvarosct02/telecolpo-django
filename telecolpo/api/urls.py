from django.urls import path
from .views import studyList

urlpatterns = [
    path('studies/', studyList),
]
