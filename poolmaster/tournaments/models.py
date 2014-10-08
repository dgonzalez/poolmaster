from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(User):
    pass
class Match(models.Model):
    player_one = models.ForeignKey(Player, related_name='%(class)s_player1')
    player_two = models.ForeignKey(Player, related_name='%(class)s_player2')
