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

        team_obj = get_object_or_404(Team, slug=self.kwargs['team'])

        context = super(RosterTemplateView, self).get_context_data(**kwargs)
        context['team'] = team_obj
        context['current_playfors'] = self.sort_playfors(
            team_obj.get_current_playfors()
        )
        context['former_playfors'] = team_obj.get_former_playfors()[:11]
        context['current_coachfors'] = self.sort_coachfors(
            team_obj.get_current_coachfors())
        context['seasons'] = Season.objects.filter(
            enrolled=team_obj).order_by('-end_date')

        return context


    # sort the list by injury reserve then positon then number
    # position G < D < M < F
    @staticmethod
    def sort_playfors(playfors):

        current_playfor_list = list(playfors)
        current_playfor_list = sorted(
            current_playfor_list,
            key=lambda x:
                ( x.injury_reserve, 0, x.number ) if x.player.position=='G'
                else ( x.injury_reserve, 1, x.number ) if x.player.position=='D'
                else ( x.injury_reserve, 2, x.number ) if x.player.position=='M'
                else ( x.injury_reserve, 3, x.number ) if x.player.position=='F'
                else ( x.injury_reserve, 4, x.number )
        )

        return current_playfor_list

    # sort the list by responsibility Coach < Assitant Coach < Manager
    @staticmethod
    def sort_coachfors(coachfors):

        current_coachfor_list = list(coachfors)
        current_coachfor_list = sorted(current_coachfor_list,
            key=lambda x:
                0 if x.responsibility=='C'
                else 1 if x.responsibility=='A'
                else 2 if x.responsibility=='M'
                else 3
        )

        return current_coachfor_list


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

        context = super(
            MatchdayListView,
            self
            ).get_context_data(**kwargs)

        context['season'] = self.season

        return context


def standings(request, classification, competition, season):

    season_obj = Season.get_season_by_slugs(
        classification,
        competition,
        season
    )

    teams_list = Team.objects.filter(season=season_obj)
    games_played_in_season = Game.objects.filter(matchday__season=season_obj).filter(played=True)

    for team in teams_list:

        games_of_team = games_played_in_season.filter(Q(home_team=team) | Q(away_team=team))

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

    teams_list.order_by('points')

    current_and_next_matchday_list = Matchday.objects.filter(
        season=season_obj
    ).filter(
        date__gt=(datetime.date.today() - datetime.timedelta(days=7))
    ).order_by('date')[:2]

    template = loader.get_template('stats/standings.html')
    context = RequestContext(request, {
        'season': season_obj,
        'teams': teams_list,
        'matchdays': current_and_next_matchday_list,
    })
    return HttpResponse(template.render(context))
