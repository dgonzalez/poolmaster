from django.contrib import admin
from tournaments.models import Player, Match, Event, Department

# Register your models here.
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Event)
admin.site.register(Department)
