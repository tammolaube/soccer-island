import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q
from django.views.generic import TemplateView
from django.views.generic.list import ListView

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
        games_played = season.get_games_played()

        context = super(StandingsTemplateView, self).get_context_data(**kwargs)

        context['season'] = season
        context['standings'] = self.calculate_standings(teams, games_played)
        context['matchdays'] = Matchday.objects.filter(
            season=season,
            date__gt=(datetime.date.today() - datetime.timedelta(days=7))
        ).order_by('date')[:2]

        return context

    @staticmethod
    def calculate_standings(teams, games_played):

        for team in teams:

            games_of_team = games_played.filter(
                Q(home_team=team) | Q(away_team=team)
            )
            team.num_games = games_of_team.count()
            team.num_wins = 0
            team.num_draws = 0
            team.num_losses = 0
            team.num_scored_goals = 0
            team.num_conceded_goals = 0

            for game in games_of_team:

                if game.get_winner() == team:
                    team.num_wins += 1
                elif game.get_winner() == None:
                    team.num_draws += 1
                else:
                    team.num_losses += 1

                if team == game.home_team:
                    team.num_scored_goals += game.get_home_goals().count()
                    team.num_conceded_goals += game.get_away_goals().count()
                else:
                    team.num_scored_goals += game.get_away_goals().count()
                    team.num_conceded_goals += game.get_home_goals().count()

            team.num_points = team.num_draws + team.num_wins * 3

        return sorted(teams, key=lambda team: team.num_points, reverse=True)
