from django.urls import path

from accounts.api_endpoinds.Profile.Register.views import *


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register-user'),
    path('register/confirm/', RegisterConfirmAPIView.as_view(), name='register-confirm'),
]