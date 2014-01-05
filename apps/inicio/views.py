from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'inicio/index.html'


class Index2(TemplateView):
    template_name = 'inicio/index2.html'