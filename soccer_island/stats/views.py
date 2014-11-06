from django.http import HttpResponse
from django.template import RequestContext, loader

from stats.models import Person

def home(request):
    template = loader.get_template('stats/home.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

def season_overview(request, classification, competition, season):
    template = loader.get_template('stats/stats.html')
    context = RequestContext(request, {
        'classification': classification,
        'competition': competition,
        'season': season,
    })
    return HttpResponse(template.render(context))
