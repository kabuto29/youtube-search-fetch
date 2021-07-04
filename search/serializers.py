from rest_framework import serializers
from search.models import videos

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields = ['id','title','description','publishedat','thumbnails']
