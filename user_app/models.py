from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    phone = models.CharField(max_length=12)
    active_code= models.CharField(max_length=6)
    def __str__(self):
        return self.username
