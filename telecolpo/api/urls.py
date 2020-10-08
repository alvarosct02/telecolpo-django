from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import study_list

urlpatterns = [
    path('studies', study_list),
    path('login', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
