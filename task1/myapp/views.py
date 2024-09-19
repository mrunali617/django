from django.http import HttpResponse
from .models import MyModel
from django.utils import timezone

def create_my_model_instance(request):
    print(f"Object creation started at {timezone.now()}")
    MyModel.objects.create(name="Test Object")  # This will trigger the signal
    print(f"Object creation finished at {timezone.now()}")
    return HttpResponse("MyModel instance created!")
