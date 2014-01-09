from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
                       # url(r'^BibliotecaVirtual/', include('BibliotecaVirtual.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       #IMAGENES
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, }),

                       #INICIO
                       url(r'^', include('apps.inicio.urls')),

                       #AUTORES
                       url(r'^autor/', include('apps.autores.urls')),

                        #LIBROS
                       url(r'^libros/', include('apps.libros.urls')),
)
