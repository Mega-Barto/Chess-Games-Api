from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date
from games.models import Game
from games.models import Player
from games.models import Result
# Create your tests here.

class GameViewSetTests(TestCase):
    def setUp(self):
        self.player1 = Player.objects.create(
            last_name="Perez",
            first_name="Juan",
            elo=1400
        )
        self.player2 = Player.objects.create(
            last_name="Sevillano",
            first_name="Miguel",
            elo=1450
        )
        self.result = Result.objects.create(
            result="1/2-1/2"
        )
        self.game = Game.objects.create(
            white_id=self.player1,
            black_id=self.player1,
            moves="1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Nb8 10.d4 Nbd7 11.c4 c6 12.cxb5 axb5 13.Nc3 Bb7 14.Bg5 b4 1/2-1/2",
            result=self.result,
            date=date(2002,8,30),
            location="Manizales",
            pgn="",
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse('game-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)