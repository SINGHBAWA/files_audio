follow the following step to setup

1. Install the requirements

```
    pip install -r requirements.txt
```


2. Migrate Models
```
    python manage.py migrate
```

3. Run python server
```
    python manage.py runserver 0:8000
```


API paths:

Get List of audio files

```
    GET:  /audio/<file_type>/

    Ex- http://127.0.0.1:8000/audio/song/
        http://127.0.0.1:8000/audio/podcast/
```


Get Details of audio files

```
    GET:  /audio/<file_type>/<id>

    Ex- http://127.0.0.1:8000/audio/song/1/
        http://127.0.0.1:8000/audio/podcast/5/
```


*Used a better approach for sending file_type in url. So there a minor change in request data *
Add Audio File
```
    POST:  /audio/<file_type>/

    Ex: 
    POST: http://127.0.0.1:8000/audio/song/

    {
        "title": "Test Song",
        "duration": 78
    }

    
    POST: http://127.0.0.1:8000/audio/audiobook/

    {
        "audio_file": {
            "title": "Test Audio book",
            "duration": 70
        },
        "author_of_title": "Aman",
        "narrator": "Aman Singh"
    }

    POST: http://127.0.0.1:8000/audio/podcast/

    {
        "audio_file": {
                "title": "Test Audio book",
                "duration": 70
            },
        "participants": ["Aman", "Jones"],
        "host": "My fav host"
    }
```

Update Audio File:

```
    PUT:  /audio/<file_type>/<id>/

    Ex:
    PUT: http://127.0.0.1:8000/audio/podcast/5/

    {
        "id": 5,
        "audio_file": {
            "id": 7,
            "title": "sghwghd",
            "duration": 56,
        },
        "participants": [],
        "host": "ury76r4r74"
    }


    PUT: http://127.0.0.1:8000/audio/podcast/5/

    {
        "id": 5,
        "title": "vdgv",
        "duration": 23,
    }


    PUT: http://127.0.0.1:8000/audio/audiobook/3/
    {
        "id": 3,
        "audio_file": {
            "id": 9,
            "title": "Test Audio book",
            "duration": 70,
        },
        "author_of_title": "Aman",
        "narrator": "Aman Singh"
    }


```
