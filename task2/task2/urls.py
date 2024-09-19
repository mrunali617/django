from django.contrib import admin
from django.urls import path
from task2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-model/', views.create_my_model_instance),
]
