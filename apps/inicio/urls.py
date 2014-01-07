from django.conf.urls import patterns, url
from .views import Registrarse

urlpatterns = patterns('',
                       url(r'^$', 'django.contrib.auth.views.login',
                           {'template_name': 'inicio/index.html'}, name='login'),

                       url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',
                           name='logout'),

                       url(r'^registrarse/$', Registrarse.as_view(), name='registrarse')
)
