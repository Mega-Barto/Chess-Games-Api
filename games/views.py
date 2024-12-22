from .serializers import GameSerializer, PlayerSerializer,ResultSerializer
from .models import Game, Player, Result
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class ListResultsView(ListAPIView, CreateAPIView):
    """
    Posibles resultados de una partida
    """
    allowed_methods = ["GET", "POST"]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

class ListGamesView(ListAPIView, CreateAPIView):
    """
    Visualizar listado de Partidas, así como añadir partidas a la lista.
    """
    allowed_methods = ["GET", "POST"]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class EditGameView(RetrieveUpdateDestroyAPIView):
    """
    Visualizar la información de una partida en particular, así como modificarla o hacer un eliminado físico de esta.
    """
    allowed_methods = ["GET", "PATCH", "DELETE"]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class ListPlayersView(ListAPIView, CreateAPIView):  # /api/players/ https://www.cdrf.co/3.14/rest_framework.generics/ListAPIView.html
    """
    Visualizar listado de Jugadores, así como añadir un nuevo jugador a la lista.
    """
    allowed_methods = ["GET", "POST"]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class EditPlayerView(RetrieveUpdateDestroyAPIView):
    """
    Visualizar la información de un Jugador en particular, así como modificarlo o hacer un eliminado físico de este.
    """
    allowed_methods = ["GET", "PATCH", "DELETE"]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    