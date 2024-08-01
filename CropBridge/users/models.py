from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
