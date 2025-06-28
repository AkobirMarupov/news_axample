from rest_framework import serializers

from news.models import Category

class CategoryUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        read_only_fields = ['id']