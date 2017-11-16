from rest_framework import serializers
from games.models import Game
from games.models import GameCategory
from games.models import Player
from games.models import PlayerScore
from django.contrib.auth.models import User

class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'games')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    # 소유자 사용자 이름만 표시 (읽기 전용)
    owner = serializers.ReadOnlyField(source='owner.username')
    # 게임 id 대신 게임 카테고리 이름을 보여준다.
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')
    # SlugRelatedField는 고유 슬러그 속성, 즉 디스크립션에 의해 관계 대상을 나타내는 읽기/쓰기 필드

    class Meta:
        model = Game
        depth = 4
        fields = (
            'url',
            'owner',
            'game_category',
            'name',
            'release_date',
            'played'
        )

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail')
    
    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    # 게임 상세보기
    game = GameSerializer()
    # player는  포함 될 것이므로 따로 추가하지않는다.
    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game',
        )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        )

class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )