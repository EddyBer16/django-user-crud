from django.db import models


# Create your models here.
class UserDjango(models.Model):
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username
