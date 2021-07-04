from django.urls import path
from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path('videoList',views.VideoBaseView.as_view(),name = 'list'),
    path('dumpData',views.getVideosAuto,name = 'dump')
]