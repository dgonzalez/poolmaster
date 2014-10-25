from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from tournaments.models import Match, Event, Player, Department

# Serializers define the API representation.
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'id', 'department')

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('player_one', 'player_two', 'winner')
        depth = 0

class AllMatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('player_one', 'player_two', 'winner')
        read_only = ('player_one', 'player_two', 'winner') 
        depth = 2


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name',)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)

# ViewSets define the view behavior.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class AllMatchesViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = AllMatchesSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'allmatches', AllMatchesViewSet)
router.register(r'events', EventViewSet)
router.register(r'departments', DepartmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
]

