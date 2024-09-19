from django.http import HttpResponse
from .models import MyModel
from django.db import transaction

def create_my_model_instance(request):
    with transaction.atomic():
        MyModel.objects.create(name="Test Object")
        # Uncomment the following line to simulate a rollback
        # raise Exception("Simulated error to test transaction rollback")
    return HttpResponse("MyModel instance created!")
