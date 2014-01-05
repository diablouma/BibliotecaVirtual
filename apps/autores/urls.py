from apps.autores.views import RegistrarAutor, ReportarAutor

__author__ = 'diablouma'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^registrar/$', RegistrarAutor.as_view(), name="registrar_autor"),
                       url(r'^reportar/$', ReportarAutor.as_view(), name="reportar_autor"),
)
