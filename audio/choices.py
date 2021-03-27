
class AudioFileTypeChoices:
    SONG = "song"
    PODCAST = "podcast"
    AUDIOBOOK = "audiobook"

    CHOICES = (
        (SONG, SONG),
        (PODCAST, PODCAST),
        (AUDIOBOOK, AUDIOBOOK)
    )

    NESTED_TYPES = [
        PODCAST, 
        AUDIOBOOK
    ]
