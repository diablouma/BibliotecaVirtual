from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from apps.autores.models import Autor
from apps.libros.models import Libro
from django.core import serializers


class BuscarView(TemplateView):
    template_name = 'libros/buscar.html'

    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        libros = Libro.objects.filter(nombre__contains=buscar)
        print libros
        if libros:
            datos = []

            for libro in libros:
                autores = libro.autor.all()
                datos.append(dict([(libro, autores)]))

            return render(request, 'libros/buscar.html', {'datos': datos})

        else:
            autores = Autor.objects.filter(nombre__contains=buscar)
            return render(request, 'libros/buscar.html',
                          {'autores': autores, 'autor': True})


class BusquedaView(ListView):
    model = Autor
    template_name = 'libros/busqueda.html'
    #recoge en la variable autores todo lo q venga
    #del modelo autor
    context_object_name = 'autores'


class BusquedaAjaxView(TemplateView):
    def get(self, request, *args, **kwargs):
        id_autor = request.GET['id']
        libros = Libro.objects.filter(autor__id=id_autor)
        data = serializers.serialize('json', libros, fields=('nombre', 'resumen'))

        return HttpResponse(data, mimetype='application/json')
