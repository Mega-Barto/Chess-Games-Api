from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Result(models.Model):
    result = models.TextField(max_length=7)
    
    def __str__(self):
        return f'{self.result},'

class Player(models.Model):
    last_name = models.TextField(max_length=30)
    first_name = models.TextField(max_length=30)
    elo = models.IntegerField(default=0, validators=[MinValueValidator(0) ,MaxValueValidator(4000)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    

class Game(models.Model):
    white_id = models.ForeignKey(Player, on_delete=models.CASCADE,  related_name="played_as_white")
    black_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="played_as_black")
    moves = models.TextField(max_length=3000)
    #total_moves = models.IntegerField() agregadas eventualmente
    #eco = models.TextField(max_length=3)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.TextField(max_length=50)
    pgn = models.TextField(null=True, max_length=100)

    def __str__(self):
        return f'moves: {self.moves}, {self.date}, {self.white}, {self.black}'
    
    