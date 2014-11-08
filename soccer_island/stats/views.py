import datetime

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.db.models import F, Q

from stats.models import Classification, Competition, Season, Team, Player, PlayFor

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

    # gets former playfors
    former_playfors_qs = PlayFor.objects.filter(
        team__slug=team,
        to_date__lt=datetime.date.today()
    ).order_by(
        'to_date'
    )

    seasons_qs = Season.objects.filter(enrolled=team_obj).order_by('-start_date')

    template = loader.get_template('stats/roster.html')
    context = RequestContext(request, {
        'team': team_obj,
        'current_playfors': current_playfor_list,
        'former_playfors': former_playfors_qs,
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
