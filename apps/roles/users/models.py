from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
    id = models.CharField(max_length=100, blank=True, auto_created=True, primary_key=True, unique=True)
