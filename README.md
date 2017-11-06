# Restful Python Web Services

##### info

- python==3.5
- django==1.11.6
- djangorestframework==3.7.1

#####API view code

```shell
games/views.py
```

##### Model

```shell
games/models.py
```

##### RAPI example

Input

```shell
curl -X GET 127.0.0.1:8000/games/
```

or

```shell
http 127.0.0.1:8000/games/
```

Output

```shell
HTTP/1.0 200 OK
Content-Length: 374
Content-Type: application/json
Date: Mon, 06 Nov 2017 04:51:56 GMT
Server: WSGIServer/0.2 CPython/3.5.2
X-Frame-Options: SAMEORIGIN

[
    {
        "game_category": "3D RPG",
        "id": 2,
        "name": "Angry Birds RPG",
        "played": false,
        "release_date": "2017-10-27T17:58:17.899425Z"
    },
    {
        "game_category": "2D mobile arcade",
        "id": 1,
        "name": "Smurfs Jungle",
        "played": false,
        "release_date": "2017-10-27T17:58:17.899425Z"
    },
    {
        "game_category": "3D",
        "id": 3,
        "name": "Tomb Raider Extreme Edition",
        "played": false,
        "release_date": "2016-05-18T03:02:00.776594Z"
    }
]
```

