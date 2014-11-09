import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q
from django.views.generic.list import ListView

from stats.models import Classification, Competition, Season, Team, Player, PlayFor, CoachFor, Matchday

def get_season_by_slugs(classification, competition, season):
    """
    This returns the season object or None.
    Slugs for classification, competition and season are
    unique. So we can use .get() instead of .filter().
    """
    # SELECT t.name FROM Team t
    # JOIN season s ON t.season=s.id
    # JOIN competition co ON s.competition=co.id
    # JOIN classfication cl ON co.classification=cl.id
    # WHERE s.slug=season AND co.slug=competition AND cl.slug=classification;

    classification_obj = get_object_or_404(Classification, slug=classification)

    competition_obj = get_object_or_404(Competition,
        classification=classification_obj,
        slug=competition
    )

    season_obj = get_object_or_404(Season,
        competition=competition_obj,
        slug=season
    )

    return season_obj

def roster(request, team):
    team_obj = get_object_or_404(Team, slug=team)

    # gets all current playfors
    current_playfors_qs = PlayFor.objects.filter(
        team__slug=team,
    ).exclude(
        to_date__lt=datetime.date.today()
    )

    # make it a list; evaluate the query set (make select to the db)
    # sort the list by injury reserve then positon then number
    current_playfor_list = list(current_playfors_qs)
    current_playfor_list = sorted(current_playfor_list,
        key=lambda x:
            ( x.injury_reserve, 0, x.number ) if x.player.position=='G'
            else ( x.injury_reserve, 1, x.number ) if x.player.position=='D'
            else ( x.injury_reserve, 2, x.number ) if x.player.position=='M'
            else ( x.injury_reserve, 3, x.number ) if x.player.position=='F'
            else ( x.injury_reserve, 4, x.number )
    )

    # gets former playfors. the last 11
    former_playfors_qs = PlayFor.objects.filter(
        team__slug=team,
        to_date__lt=datetime.date.today()
    ).order_by(
        'to_date'
        )[:11]

    # gets all current coachfors
    current_coachfors_qs = CoachFor.objects.filter(
        team__slug=team,
    ).exclude(
        to_date__lt=datetime.date.today()
    )

    # make it a list; evaluate the query set (make select to the db)
    # sort the list by responsibility Coach < Assitant Coach < Manager
    current_coachfor_list = list(current_coachfors_qs)
    current_coachfor_list = sorted(current_coachfor_list,
        key=lambda x:
            0 if x.responsibility=='C'
            else 1 if x.responsibility=='A'
            else 2 if x.responsibility=='M'
            else 3
    )

    # get seasons the team is enrolled in
    seasons_qs = Season.objects.filter(enrolled=team_obj).order_by('-end_date')

    # get template and pass the collected data via context; return the view
    template = loader.get_template('stats/roster.html')
    context = RequestContext(request, {
        'team': team_obj,
        'current_playfors': current_playfor_list,
        'former_playfors': former_playfors_qs,
        'current_coachfors': current_coachfor_list,
        'seasons': seasons_qs,
    })
    return HttpResponse(template.render(context))

def season_teams(request, classification, competition, season):
    season_obj = get_season_by_slugs(classification, competition, season)
    if not season_obj:
         raise Http404

    teams = Team.objects.filter(season=season_obj)

    template = loader.get_template('stats/season_teams.html')
    context = RequestContext(request, {
        'season': season_obj,
        'teams': teams,
    })
    return HttpResponse(template.render(context))

class MatchdayListView(ListView):
    model = Matchday
    context_object_name = 'matchday_list'
    template_name = 'stats/schedule.html'
    season = None

    def get_queryset(self, **kwargs):
        self.season = get_season_by_slugs(
            self.kwargs['classification'],
            self.kwargs['competition'],
            self.kwargs['season']
        )
        return Matchday.objects.filter(season=self.season).order_by('date')

    def get_context_data(self, **kwargs):
        context = super(MatchdayListView, self).get_context_data(**kwargs)
        context['season'] = self.season
        return context

def season_overview(request, classification, competition, season):
    classifications_qs = Classification.objects.filter(slug=classification)
    competitions_qs = Competition.objects.filter(classification__in=classifications_qs, slug=competition)
    seasons_qs = Season.objects.filter(competition__in=competitions_qs, slug=season)
    teams = Team.objects.filter(season__in=seasons_qs)

    template = loader.get_template('stats/season_overview.html')
    context = RequestContext(request, {
        'classification': classification,
        'competition': competition,
        'season': season,
        'teams': teams,
    })
    return HttpResponse(template.render(context))
