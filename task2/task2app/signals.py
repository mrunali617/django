from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import threading

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal handled in thread: {current_thread}")
