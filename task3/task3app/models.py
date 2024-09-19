from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LogEntry(models.Model):
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
