from audio.choices import AudioFileTypeChoices

class AudioFileTypeConverter:
    regex = '|'.join(dict(AudioFileTypeChoices.CHOICES).keys())

    def to_python(self, value):
        return value
