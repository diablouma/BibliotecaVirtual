from django.conf.urls import patterns, url
from apps.libros.views import BuscarView, BusquedaView, BusquedaAjaxView

urlpatterns = patterns('',
                       url(r'^buscar/$', BuscarView.as_view(), name='buscar'),
                       url(r'^busqueda/$', BusquedaView.as_view(), name='busqueda'),
                       url(r'^busqueda_ajax/$', BusquedaAjaxView.as_view()),
)
