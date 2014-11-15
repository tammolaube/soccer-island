import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q, Prefetch
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db import connection

from stats.models import Classification, Competition, Season, Team, Player, PlayFor, CoachFor, Matchday, Game, Goal


class TeamTemplateView(TemplateView):

    template_name = 'stats/team.html'

    def get_context_data(self, **kwargs):

        team = get_object_or_404(Team, slug=self.kwargs['team'])

        context = super(TeamTemplateView, self).get_context_data(**kwargs)
        context['team'] = team
        context['current_playfors'] = self.sort_playfors(
            team.get_current_playfors()
        )
        context['former_playfors'] = team.get_former_playfors()[:11]
        context['current_coachfors'] = self.sort_coachfors(
            team.get_current_coachfors()
        )
        context['seasons'] = Season.objects.filter(
            enrolled=team
        ).order_by('-end_date')

        return context


    # sort the list by injury reserve then positon then number
    # position G < D < M < F
    @staticmethod
    def sort_playfors(playfors):

        return sorted(playfors,
                key=lambda x:
                    ( x.injury_reserve, 0, x.number ) if x.player.position=='G'
                    else ( x.injury_reserve, 1, x.number ) if x.player.position=='D'
                    else ( x.injury_reserve, 2, x.number ) if x.player.position=='M'
                    else ( x.injury_reserve, 3, x.number ) if x.player.position=='F'
                    else ( x.injury_reserve, 4, x.number )
            )


    # sort the list by responsibility Coach < Assitant Coach < Manager
    @staticmethod
    def sort_coachfors(coachfors):

        return sorted(coachfors,
                key=lambda x:
                    0 if x.responsibility=='C'
                    else 1 if x.responsibility=='A'
                    else 2 if x.responsibility=='M'
                    else 3
            )


class MatchdayListView(ListView):

    model = Matchday
    context_object_name = 'matchday_list'
    template_name = 'stats/schedule.html'
    season = None

    def get_queryset(self, **kwargs):

        self.season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        return Matchday.objects.filter(
                season=self.season
            ).order_by('date').\
                prefetch_related('games__home_team',
                    'games__away_team', 'games__field')

    def get_context_data(self, **kwargs):

        context = super(MatchdayListView, self).get_context_data(**kwargs)
        context['season'] = self.season

        return context


class StandingsTemplateView(TemplateView):

    template_name = 'stats/standings.html'

    def get_context_data(self, **kwargs):

        season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        context = super(StandingsTemplateView, self).get_context_data(**kwargs)
        context['season'] = season
        context['standings'] = season.standings()
        context['matchdays'] = season.last_and_next_matchdays()

        return context


class DisciplinaryListView(ListView):

    model = PlayFor
    context_object_name = 'playfor_list'
    template_name = 'stats/disciplinary.html'
    season = None

    def get_queryset(self, **kwargs):

        self.season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        return self.order_by_cards(
                self.season.booked_playfors(),
                self.season
            )

    def get_context_data(self, **kwargs):

        context = super(DisciplinaryListView, self).get_context_data(**kwargs)
        context['season'] = self.season

        return context

    @staticmethod
    def order_by_cards(playfors, season):

        for playfor in playfors:

            playfor.num_yellow_cards =\
                playfor.count_yellow_cards_per(season)
            playfor.num_red_cards =\
                playfor.count_red_cards_per(season)

        return sorted(
                playfors,
                key=lambda x: (x.num_red_cards, x.num_yellow_cards),
                reverse=True
            )

class GoalsListView(TemplateView):

    template_name = 'stats/goals.html'

    def get_context_data(self, **kwargs):

        season = Season.get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )

        context = super(GoalsListView, self).get_context_data(**kwargs)
        context['season'] = season
        context['scorers'] = season.with_teams(season.scorers())
        context['assistants'] = season.with_teams(season.assistants())

        return context
