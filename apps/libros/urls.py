from django.conf.urls import patterns, url
from apps.libros.views import BuscarView

urlpatterns = patterns('',
                       url('^buscar/$', BuscarView.as_view(), name='buscar')
)
