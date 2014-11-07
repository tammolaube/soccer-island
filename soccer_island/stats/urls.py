from django.conf.urls import patterns, url
from django.views import generic

from stats import views

urlpatterns = patterns('',
    url(r'^/?$',
        generic.TemplateView.as_view(template_name='stats/home.html'),
        name='home'
    ),
    url(r'^team/(?P<team>.*)/$',
        views.roster,
        name='roster'
    ),
    url(r'^teams/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/$',
        views.season_teams,
        name='season_teams'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/$',
        views.season_overview,
        name='season_overview'
    ),
)
