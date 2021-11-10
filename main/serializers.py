from rest_framework import serializers
from .models import Video, VideoQuality


class VideoResolution(serializers.ModelSerializer):
    class Meta:
        model = VideoQuality
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    resolutions = VideoResolution(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
