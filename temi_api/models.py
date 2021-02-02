from django.db import models


# Create your models here.
class Credential(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=30)
    user_json = models.JSONField()
