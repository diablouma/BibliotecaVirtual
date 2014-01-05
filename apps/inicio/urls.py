from django.conf.urls import patterns, include, url
from apps.inicio.views import Index
from .views import Index2

urlpatterns = patterns('',
    url(r'^$', Index.as_view()),
    url(r'^index/$', Index2.as_view()),
)
