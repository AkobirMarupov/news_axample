from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from common.models import MediaFile
from common.api_endpoinds.MediaFileDElete.serializers import MediaFileDeleteSerializer


class MediaFileDestroyAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())

        return Response({"message": "File muvaffaqiyatlu uchirildi"}, status=204)
    
    def perform_destroy(self, instance):
       
        if instance.file:
            instance.file.delete(save=False)
        super().perform_destroy(instance)