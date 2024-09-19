from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
from django.utils import timezone
import time

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal triggered at {timezone.now()}")
        time.sleep(5) 
        print(f"Signal processing done at {timezone.now()}")
