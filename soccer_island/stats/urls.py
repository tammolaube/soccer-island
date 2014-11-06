from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^/?$', views.home, name='home'),
    url(r'^(?P<classification>\w{1,32})/(?P<competition>\w{1,64})/(?P<season>\w{9})/$', views.season_overview, name='season_overview'),
)
