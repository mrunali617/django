from django.http import HttpResponse
from .models import MyModel
from django.db import transaction

def create_my_model_instance(request):
    with transaction.atomic():
        MyModel.objects.create(name="Test Object")
    return HttpResponse("MyModel instance created!")
