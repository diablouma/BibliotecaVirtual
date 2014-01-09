from apps.libros.models import Libro
from django.contrib import admin

__author__ = 'diablouma'


class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'resumen', 'imagen_portadas')
    list_filter = ('autor',)
    search_fields = ('nombre', 'autor__nombre')
    #aqui deben estar atributos que esten tmb en list_display
    #el primer valor debe ser diferente al de list_display
    list_editable = ('nombre', 'resumen')

    #con esto se muestra un pick list en relacion manytomany
    #autor es el campo manytomany en libro
    filter_horizontal = ('autor',)

    def imagen_portadas(self, libro):
        url = libro.traer_url_portadas()
        tag = "<img src=%s>" % url
        return tag

    imagen_portadas.allow_tags = True


admin.site.register(Libro, LibroAdmin)
