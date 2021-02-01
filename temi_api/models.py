from django.db import models


# Create your models here.
class Credential(models.Model):
    serialNumber = models.CharField(max_length=100)
    userJson = models.JSONField()
