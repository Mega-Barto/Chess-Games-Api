from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import GameSerializer, PlayerSerializer
from .models import Game, Player
from .permissions import IsAdminOrReadOnly

class GameViewSet(viewsets.ModelViewSet):
    """
    Partidas Registradas
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class PlayerViewSet(viewsets.ModelViewSet):
    """
    Jugadores Registrados
    """
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @action(["GET"], detail=False, url_path="list-highest-elo-players")
    def list_highest_elo_players(self, request):
        player_list = self.get_queryset().order_by('-elo')[:2].values() #Revisar el filtro [:2]
        print(player_list)
        return Response(player_list)
    
    #@action([""])