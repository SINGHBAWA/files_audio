from django.urls import path, include
from django.urls import register_converter
from audio.views import AudioView, AudioListView
from audio.converters import AudioFileTypeConverter

register_converter(AudioFileTypeConverter, 'ft')


urlpatterns = [
    path('<ft:file_type>/', AudioView.as_view()),
    path('<ft:file_type>/<int:pk>/', AudioListView.as_view()),
]