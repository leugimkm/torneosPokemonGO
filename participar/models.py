from django.db import models
from django.contrib.auth.models import User

class Participar(models.Model):
    ASISTIR_CHOICES = (
        ('Si','Si'),
        ('No','No'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    asistir = models.CharField(max_length=2, null=True, choices=ASISTIR_CHOICES, default='No')

    class Meta:
        verbose_name_plural = 'participantes'

    def __str__(self):
        return f"{self.user}: {self.asistir} va a asistir"