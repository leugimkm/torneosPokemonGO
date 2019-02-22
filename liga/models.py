from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class Usuario(models.Model):
    """Informacion del usuario"""
    nick = models.CharField(max_length=40)
    ELEGIR_SEXO = (
        ('M','Masculino'),
        ('F','Femenino')
    )
    sexo = models.CharField(max_length=1, choices=ELEGIR_SEXO)
    
    class Meta:
        abstract = True


class Entrenador(Usuario):
    """Informacion del entrenador"""
    celular = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=30, blank=True)
   
    class Meta:
        ordering = ['nick']

    def __str__(self):
        return f"{self.nick}"