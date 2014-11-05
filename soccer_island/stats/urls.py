from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^/?$', views.home, name='home'),
    url(r'^stats/(?P<competition>\w{4,6})/(?P<season>\d{4})/$', views.stats, name='stats'),
)
