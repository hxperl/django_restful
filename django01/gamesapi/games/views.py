from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from games.models import Game
from games.serializers import GameSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    """
    HttpResponse 클래스는 내용이 문자열로 된 HTTP 응답을 리턴한다.
    JSONResponse 클래스는 HttpResponse 클래스를 상속받아 구현했고 내용을 JSON으로 렌더링한다.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def game_list(request):
    """
    모든 게임을 나열하거나 새 게임을 생성한다.
    request 인자로 HttpRequest 인스턴스를 받는다.
    GET, POST 두 가지 동사를 처리할 수 있다.
    """

    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return JSONResponse(games_serializer.data)

    elif request.method == 'POST':
        games_serializer = GameSerializer(data=request.data)
        if games_serializer.is_valid():
            games_serializer.save()
            return Response(games_serializer.data, status=status.HTTP_201_CREATED)
        return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST'])
def game_detail(request, pk):
    """
    기존의 게임을 검색, 업데이트, 삭제한다.
    request 인자로 HttpRequest 인스턴스를 받고 pk 인자로는 검색, 업데이트, 삭제할 게임의 기본 키 또는 식별자를 받는다.
    """

    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)

    elif request.method == 'PUT':
        game_serializer = GameSerializer(game, data = request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data)
        return Response(game_serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)