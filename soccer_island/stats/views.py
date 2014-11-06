from django.http import HttpResponse
from django.template import RequestContext, loader

from stats.models import Classification, Competition, Season, Team

def home(request):
    template = loader.get_template('stats/home.html')
    context = RequestContext(request, {
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
