from django.urls import path

from common.api_endpoinds.MediaFileDElete.views import *
from common.api_endpoinds.MediaFileUpload.views import *


app_name = 'common'

urlpatterns = [

    path("media/upload/", MediaFileCreateAPIView.as_view(), name="media-upload"),
    path("media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name="media-delete"),
]