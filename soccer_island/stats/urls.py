from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^persons/', views.persons, name='persons'),
)
