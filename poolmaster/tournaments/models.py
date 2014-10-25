from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department)
    user = User
    def __unicode__(self):
        return self.name

class Match(models.Model):
    player_one = models.ForeignKey(Player, related_name='matches_player_1')
    player_two = models.ForeignKey(Player, related_name='matches_player_2')
    winner = models.ForeignKey(Player, related_name='winner')

class Event(models.Model):
    event_name = models.CharField(max_length = 100)
