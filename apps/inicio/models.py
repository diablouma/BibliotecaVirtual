from django.contrib.auth.models import User
from django.db import models


class Perfiles(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.IntegerField()

    def __unicode__(self):
        return self.usuario.username
