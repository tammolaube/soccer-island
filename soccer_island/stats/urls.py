from django.conf.urls import patterns, url
from django.views import generic

from stats import views

urlpatterns = patterns('',
    url(r'^/?$',
        generic.TemplateView.as_view(template_name='stats/home.html'),
        name='home'
    ),
    url(r'^teams/(?P<team>.*)/$',
        views.roster,
        name='roster'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/$',
        views.standings,
        name='standings'
    ),
    url(r'^season/(?P<classification>.*)/(?P<competition>.*)/(?P<season>\d{4}-\d{4})/schedule/$',
        views.MatchdayListView.as_view(),
        name='matchday_list'
    ),
)
