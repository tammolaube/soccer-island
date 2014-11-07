import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q

from stats.models import Classification, Competition, Season, Team, Player

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

    players_qs = Player.objects.filter(
        playfor__team__slug=team
    ).filter(
        Q(playfor__to_date__gte=datetime.date.today()) | Q(playfor__to_date__isnull=True),
        playfor__from_date__lte=datetime.date.today(),
        ).distinct()

    # evaluate the query set. make select to the db
    player_list = list(players_qs)
    player_list = sorted(player_list, key=lambda x: 0 if x.position=='G' else 1 if x.position=='D' else 2 if x.position=='M' else 3 if x.position=='A' else 4)

    seasons_qs = Season.objects.filter(enrolled=team_obj).order_by('-start_date')

    template = loader.get_template('stats/roster.html')
    context = RequestContext(request, {
        'team': team_obj,
        'players': player_list,
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
