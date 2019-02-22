from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Participar

@receiver(post_save, sender=User)
def create_participar(sender, instance, created, **kwargs):
    if created:
        Participar.objects.create(user=instance)
    instance.participar.save()
    
@receiver(post_save, sender=User)
def save_participar(sender, instance, **kwargs):
    instance.participar.save()
