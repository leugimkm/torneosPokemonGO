from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

ELEGIR_SEXO = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    )
ELEGIR_TEAM = (
        ('Valor','Valor'),
        ('Mystic','Mystic'),
        ('Instinct','Instinct')
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    
    sexo = models.CharField(max_length=9, choices=ELEGIR_SEXO)
    
    team = models.CharField(max_length=8, choices=ELEGIR_TEAM)
    nivel = models.PositiveSmallIntegerField(
        default=1, 
        validators=[MaxValueValidator(40), MinValueValidator(1)] 
    )
    
    def __str__(self):
        return f"Perfil de {self.user.username} - team {self.team} - nivel {self.nivel} - sexo {self.sexo}"


