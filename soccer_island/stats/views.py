import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q, Prefetch
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db import connection

from stats.models import Classification, Competition, Season, Team, Player, PlayFor, CoachFor, Matchday, Game, Goal


class RosterTemplateView(TemplateView):

    template_name = 'stats/roster.html'

    def get_context_data(self, **kwargs):

        team = get_object_or_404(Team, slug=self.kwargs['team'])

        context = super(RosterTemplateView, self).get_context_data(**kwargs)
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
            ).order_by('date')

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
        teams = season.get_teams()

        context = super(StandingsTemplateView, self).get_context_data(**kwargs)

        context['season'] = season
        context['standings'] = self.calculate_standings(teams)
        context['matchdays'] = Matchday.objects.filter(
            season=season,
            date__gt=(datetime.date.today() - datetime.timedelta(days=7))
        ).order_by('date').prefetch_related('games')[:2]

        return context

    @staticmethod
    def calculate_standings(teams):

        teams = teams.prefetch_related(
            Prefetch('home__goals__scored_for'),
            Prefetch('away__goals__scored_for')
        )

        for team in teams:

            team.num_games = 0
            team.num_wins = 0
            team.num_draws = 0
            team.num_losses = 0
            team.num_scored_goals = 0
            team.num_conceded_goals = 0
            team.goal_diff = 0

            for game in list(team.home.all()) + list(team.away.all()):

                if not game.played:
                    continue

                team.num_games += 1

                scored_goals = 0
                conceded_goals = 0

                for goal in game.goals.all():

                    if goal.scored_for == team:
                        scored_goals += 1
                    else:
                        conceded_goals += 1

                team.num_scored_goals += scored_goals
                team.num_conceded_goals += conceded_goals

                if scored_goals > conceded_goals:
                    team.num_wins += 1
                elif scored_goals == conceded_goals:
                    team.num_draws += 1
                else:
                    team.num_losses += 1

            team.num_points = team.num_draws + team.num_wins * 3
            team.goal_diff = team.num_scored_goals - team.num_conceded_goals

        return sorted(teams, key=lambda team:
            (team.num_points, team.goal_diff, team.num_scored_goals),
            reverse=True
        )


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
        context['scorers'] = self.annotate_teams(season.scorers(), season)
        context['assistants'] = self.annotate_teams(season.assistants(), season)

        return context

    @staticmethod
    def annotate_teams(players, season):

        players = players.prefetch_related(
            Prefetch('registered',
                queryset=Team.objects.filter(season=season),
                to_attr='teams'
            )
        )

        return players
