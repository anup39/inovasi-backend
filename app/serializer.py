from rest_framework import serializers
from .models import Facility


class FileUploadSerializer(serializers.Serializer):
    sheet = serializers.CharField()
    file = serializers.FileField()


class ShapeFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
