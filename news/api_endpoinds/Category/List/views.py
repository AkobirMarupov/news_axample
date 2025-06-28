from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import Category
from news.api_endpoinds.Category.List.serializers import CategoryListSerializers



class CategoryListGetAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = []
   
    

class CategoryRetrieveAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = []
    lookup_field = "pk"