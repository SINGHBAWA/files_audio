from django.db import models
from audio.choices import AudioFileTypeChoices

# Create your models here.

class AudioFile(models.Model):
    file_type = models.CharField(max_length=50, choices=AudioFileTypeChoices.CHOICES, default=AudioFileTypeChoices.SONG)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)


class Podcast(models.Model):
    audio_file = models.OneToOneField(AudioFile, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    participants = models.JSONField(max_length=1100, null=True, blank=True)



class AudioBook(models.Model):
    audio_file = models.OneToOneField(AudioFile, on_delete=models.CASCADE)
    author_of_title = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
