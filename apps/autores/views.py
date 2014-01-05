# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from apps.autores.models import Autor


class RegistrarAutor(CreateView):
    template_name = 'autores/registrarAutor.html'
    model = Autor
    success_url = reverse_lazy('reportar_autor')


class ReportarAutor(ListView):
    template_name = 'autores/reportarAutor.html'
    model = Autor
    context_object_name = 'autores'