from .models import AudioFile, Podcast, AudioBook
from .choices import AudioFileTypeChoices
from rest_framework import serializers

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        exclude = ('file_type',)



class NestedAudioSerializerMixin:
    
    class Meta:
        file_type = None
        model = None

    def create(self, validated_data):
        audio_file_data = validated_data.pop('audio_file')
        audio_file_data["file_type"] = self.Meta.file_type
        audio_file = AudioFileSerializer.create(AudioFileSerializer(), validated_data=audio_file_data)
        instance = self.Meta.model.objects.create(audio_file=audio_file, **validated_data)
        return instance

    
    def update(self, instance, validated_data):
        audio_file_data = validated_data.pop('audio_file')
        audio_file_data["file_type"] = self.Meta.file_type
        audio_file = AudioFileSerializer.update(AudioFileSerializer(), instance=instance.audio_file, validated_data=audio_file_data)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance



class PodcastSerializer(NestedAudioSerializerMixin, serializers.ModelSerializer):
    audio_file = AudioFileSerializer()
    participants = serializers.JSONField()

    class Meta:
        model = Podcast
        file_type = AudioFileTypeChoices.PODCAST
        fields = '__all__'
    


class AudioBookSerializer(NestedAudioSerializerMixin, serializers.ModelSerializer):
    audio_file = AudioFileSerializer()

    class Meta:
        model = AudioBook
        file_type = AudioFileTypeChoices.AUDIOBOOK
        fields = '__all__'
   