from django.contrib import admin
from stats.models import Classification
from stats.models import Address
from stats.models import Person
from stats.models import Club
from stats.models import Team
from stats.models import Player
from stats.models import PlayFor
from stats.models import Coach
from stats.models import CoachFor
from stats.models import Referee
from stats.models import Field
from stats.models import Competition
from stats.models import Season
from stats.models import Game
from stats.models import Goal
from stats.models import Card
from stats.models import Suspension
from stats.models import Matchday

class ClassificationAdmin(admin.ModelAdmin):
    exclude = ('slug',)

# Register your models here.
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayFor)
admin.site.register(Coach)
admin.site.register(CoachFor)
admin.site.register(Referee)
admin.site.register(Field)
admin.site.register(Competition)
admin.site.register(Season)
admin.site.register(Game)
admin.site.register(Goal)
admin.site.register(Card)
admin.site.register(Suspension)
admin.site.register(Matchday)
