from django.contrib import admin
from tournaments.models import Player, Match, Event

# Register your models here.
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Event)
