from django.conf.urls import patterns, url
from django.views import generic

from stats import views

REGEX_CLASSIFICATION_COMPETITION_SEASON =\
    '(?P<classification>[^/]+)/(?P<competition>[^/]+)/(?P<season>[^/]+)?/?$'

urlpatterns = patterns('',
    url(r'^/?$',
        generic.TemplateView.as_view(template_name='stats/home.html'),
        name='home'
    ),
    url(r'^login/',
        views.login_view,
        name='login'
    ),
    url(r'^logout/',
        views.logout_view,
        name='logout'
    ),
    url(r'^team/(?P<team>.*)/$',
        views.TeamTemplateView.as_view(),
        name='team'
    ),
    url(r'^game/(?P<pk>\d+)/$',
        views.GameDetailView.as_view(),
        name='game'
    ),
    url(r'^game/(?P<pk>\d+)/update/$',
        views.update_game_view,
        name='update_game'
    ),
    url(r'^overview/' + REGEX_CLASSIFICATION_COMPETITION_SEASON,
        views.OverviewTemplateView.as_view(),
        name='overview'
    ),
    url(r'^standings/' + REGEX_CLASSIFICATION_COMPETITION_SEASON,
        views.StandingsTemplateView.as_view(),
        name='standings'
    ),
    url(r'^schedule/' + REGEX_CLASSIFICATION_COMPETITION_SEASON,
        views.MatchdayListView.as_view(),
        name='schedule'
    ),
    url(r'^disciplinary/' + REGEX_CLASSIFICATION_COMPETITION_SEASON,
        views.DisciplinaryListView.as_view(),
        name='disciplinary'
    ),
    url(r'^goals/' + REGEX_CLASSIFICATION_COMPETITION_SEASON,
        views.GoalsListView.as_view(),
        name='goals'
    ),
)
