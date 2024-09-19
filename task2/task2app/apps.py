from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'task2app'

    def ready(self):
        import task2app.signals
