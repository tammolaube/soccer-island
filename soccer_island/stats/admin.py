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

class CompetitionAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class SeasonAdmin(admin.ModelAdmin):
    fields = ('label', 'competition',
        'start_date', 'end_date', 'enrolled', 'published',)

class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'classification', 'colors', 'club',)

class ClubAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class MatchdayAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class GoalAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "scored_by":
            kwargs["queryset"] = PlayFor.objects.all().select_related(
                'player__person',
                'team',
            )
        if db_field.name == "assisted_by":
            kwargs["queryset"] = PlayFor.objects.all().select_related(
                'player__person',
                'team',
            )
        if db_field.name == "game":
            kwargs["queryset"] = Game.objects.all().select_related(
                'home_team',
                'away_team',
            )
        return super(GoalAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class GameAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Teams', {
            'fields': ('home_team', 'away_team'),
            'classes': ('wide',)
        }),
        (None, {
            'fields': (
                'date',
                ('field', 'referee'),
                'played',
                'matchday',
            )
        })
    )
    list_display = ('matchday', 'home_team', 'away_team', 'date', 'played')
    list_filter = ('matchday__season', 'matchday', 'date', 'played')
    list_select_related = ('game',)

admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Club, ClubAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
admin.site.register(PlayFor)
admin.site.register(Coach)
admin.site.register(CoachFor)
admin.site.register(Referee)
admin.site.register(Field)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Card)
admin.site.register(Suspension)
admin.site.register(Matchday, MatchdayAdmin)
