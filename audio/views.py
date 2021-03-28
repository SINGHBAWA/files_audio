from django.shortcuts import render
from rest_framework import generics, response, status
from audio.models import AudioFile, Podcast, AudioBook
from audio.choices import AudioFileTypeChoices
from audio.serializers import AudioFileSerializer, AudioBookSerializer, PodcastSerializer


class AudioViewMixin:
    serializer_map = {
        AudioFileTypeChoices.SONG: AudioFileSerializer,
        AudioFileTypeChoices.PODCAST: PodcastSerializer,
        AudioFileTypeChoices.AUDIOBOOK: AudioBookSerializer,
    }
    model_map = {
        AudioFileTypeChoices.SONG: AudioFile,
        AudioFileTypeChoices.PODCAST: Podcast,
        AudioFileTypeChoices.AUDIOBOOK: AudioBook,
    }

    def get_queryset(self, *args, **kwargs):

        file_type = self.kwargs['file_type']
        queryset = self.model_map[file_type].objects.all()
        if file_type in AudioFileTypeChoices.NESTED_TYPES:
            queryset = queryset.select_related("audio_file")
        else:
            queryset = queryset.filter(file_type=file_type)
        return queryset
    
    def get_serializer_class(self, *args, **kwargs):
        file_type = self.kwargs['file_type']
        return self.serializer_map[file_type]
    
    def delete(self, request, *args, **kwargs):
        file_type = self.kwargs['file_type']
        if not file_type in dict(AudioFileTypeChoices.CHOICES):
            return response.Response("Invalid FileType", status=400)
        else:
            instance = self.get_object()
            if file_type in AudioFileTypeChoices.NESTED_TYPES:
                instance.audio_file.delete()
            else:
                instance.delete()
        return response.Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)


# ViewSets define the view behavior.
class AudioView(AudioViewMixin, generics.ListCreateAPIView):
    pass

# ViewSets define the view behavior.
class AudioListView(AudioViewMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
