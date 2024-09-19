from django.http import HttpResponse
from .models import MyModel
import threading

def create_my_model_instance(request):
    current_thread = threading.current_thread().name
    print(f"Object creation started in thread: {current_thread}")
    MyModel.objects.create(name="Test Object")
    print(f"Object creation finished in thread: {current_thread}")
    return HttpResponse("MyModel instance created!")
