from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from search.models import videos
from search.serializers import VideosSerializer
from .modifiedpagination import CursorPaginationWithOrder, PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

def getVideosAuto():
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    payload = {
        'part' : 'snippet',
        'order' : 'date',
        'q' : 'permish verma',
        'key' : 'AIzaSyD_YbFKX6b_u5px1o8SZvXu5Zxe-ONqYfo'
    }

    result = requests.get(search_url , params = payload)
    snippetList = []
    for r in result.json()['items']:
        snippetList.append(r['snippet'])
    i=0
    for r in snippetList:
        uploadData = {}
        uploadData['title'] = r['title'][:70]
        uploadData['description'] = r['description']
        uploadData['thumbnails'] = r['thumbnails']
        uploadData['publishedat'] = r['publishedAt']
        serializers = VideosSerializer(data = uploadData)
        if(serializers.is_valid()):
            i=i+1
            serializers.save()
        else:
            print(serializers.errors)
    print("added {} videos in db".format(i))

class VideoBaseView(ListAPIView):
    queryset = videos.objects.all()
    serializer_class = VideosSerializer
    pagination_class = CursorPaginationWithOrder
    filter_backends = [SearchFilter]
    search_fields = ['title']

        
    