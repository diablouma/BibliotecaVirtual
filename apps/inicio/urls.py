from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'django.contrib.auth.views.login',
                           {'template_name': 'inicio/index.html'}, name='login'),

                       url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',
                           name='logout')
)
