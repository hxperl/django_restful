# Django restful project

##### info

- python==3.5
- django==1.11.6
- djangorestframework==3.7.1
- database == PostgreSQL 9.5

###내용 정리

##### 1.1 모델생성

django.db.models.Model 서브 클래스 생성

##### 1.2 Serializer

모델 인스턴스와 파이썬 프리미티브 사이의 중개자

##### 1.3 Parser & Renderer

파이썬 프리미티브와 HTTP 요청&응답 사이의 중개자

#####1.4 urlpatterns

url을 뷰에 전달 

##### 2.1 @api_view 데코레이터

함수 기반 뷰를 rest_framework.views.APIView 클래스의 서브 클래스로 변환하는 래퍼

##### 2.2 브라우저블 API

요청이 text/html을 요청 헤더의 Content-type 키 값으로 지정할 때마다 각 자원에 대해 인간 친화적인 HTML 출력을 생성

#####2.3 rest_framework.serializers.ModelSerializer 클래스

기본 필드 집합과 기본 유효성 검사기 집합을 자동으로 채움

create 및 update 메소드의 기본 구현 제공

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

