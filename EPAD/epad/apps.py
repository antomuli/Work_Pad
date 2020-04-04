from django.apps import AppConfig


class EpadConfig(AppConfig):
    name = 'epad'

    def ready(self):
        import epad.signals
