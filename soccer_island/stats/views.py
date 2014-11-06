from django.http import HttpResponse
from django.template import RequestContext, loader

from stats.models import Team

def home(request):
    template = loader.get_template('stats/home.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

def season_overview(request, classification, competition, season):
    teams = Team.objects.filter(
        season__slug=season,
        season__competition__slug=competition,
        season__competition__classifcation__slug=classification
    )

    template = loader.get_template('stats/season_overview.html')
    context = RequestContext(request, {
        'classification': classification,
        'competition': competition,
        'season': season,
        'teams': teams,
    })
    return HttpResponse(template.render(context))
