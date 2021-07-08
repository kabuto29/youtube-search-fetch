from celery.app import shared_task
from youtubeSearch.celery import app
from search.serializers import VideosSerializer
import requests


@shared_task
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