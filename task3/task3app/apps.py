from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'task3app'

    def ready(self):
        import task3app.signals
