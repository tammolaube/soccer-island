from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^/?$', views.home, name='home'),
    url(r'^(?P<classification>.*)/(?P<competition>.*)/(?P<season>.*)/$', views.season_overview, name='season_overview'),
)
