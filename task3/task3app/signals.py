# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, LogEntry
from django.db import transaction
@receiver(post_save, sender=MyModel)
def log_creation(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            LogEntry.objects.create(action=f"Created {instance.name}")
            # Uncomment the following line to simulate an error and see the rollback in action
            # raise Exception("Simulated error to test transaction rollback")
