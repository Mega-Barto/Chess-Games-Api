from rest_framework import serializers
from datetime import date
from .models import Game, Player, Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):

    days_since_played = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            'id',
            'white_id',
            'black_id',
            'moves',
            'result',
            'date',
            'days_since_played', #Esta está por fines del aprendizaje
            'location',
            'pgn',
        ]

    def validate(self, attrs):
        if attrs["black_id"] == attrs["white_id"]:
            raise serializers.ValidationError("A player cannot play against himself.")
        return attrs
    
    def get_days_since_played(self, obj):
        days_since_played_dt = date.today() - obj.date
        return days_since_played_dt.days 



class PlayerSerializer(serializers.ModelSerializer):

    played_as_black = GameSerializer(many=True, read_only=True) #Debe coincidir con el related name que aparece en el modelo
    played_as_white = GameSerializer(many=True, read_only=True) #Debe coincidir con el related name que aparece en el modelo

    class Meta:
        model = Player
        fields = [
            "id",
            "last_name",
            "first_name",
            "elo",
            "played_as_black",
            "played_as_white",
        ]
