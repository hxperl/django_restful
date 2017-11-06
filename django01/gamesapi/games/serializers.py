from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    """
    일반 동작으로도 충분하기 때문에 create 또는 update 메소드를 오버라이드 할 필요가 없다.
    """
    class Meta:
        model = Game
        fields = ('id',
                    'name',
                    'release_date',
                    'game_category',
                    'played')