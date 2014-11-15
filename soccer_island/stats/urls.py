from django.conf.urls import patterns, url
from django.views import generic

from stats import views

urlpatterns = patterns('',
    url(r'^/?$',
        generic.TemplateView.as_view(template_name='stats/home.html'),
        name='home'
    ),
    url(r'^team/(?P<team>.*)/$',
        views.TeamTemplateView.as_view(),
        name='team'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/$',
        views.StandingsTemplateView.as_view(),
        name='standings'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/schedule/$',
        views.MatchdayListView.as_view(),
        name='matchdays'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/disciplinary/$',
        views.DisciplinaryListView.as_view(),
        name='disciplinary'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/goals/$',
        views.GoalsListView.as_view(),
        name='goals'
    ),
)
