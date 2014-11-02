from django.http import HttpResponse
from django.template import RequestContext, loader

from stats.models import Person

def persons(request):
    person_list = Person.objects.all()
    template = loader.get_template('stats/persons.html')
    context = RequestContext(request, {
        'p_l': person_list,
    })
    return HttpResponse(template.render(context))
