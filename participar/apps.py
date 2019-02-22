from django.apps import AppConfig


class ParticiparConfig(AppConfig):
    name = 'participar'

    def ready(self):
        import participar.signals