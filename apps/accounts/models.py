from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    LEVEL_USER = [
        ('p','Pro'),
        ('l','Lite'),
    ]

    age = models.PositiveIntegerField(null=True,blank=True)
    level = models.CharField(max_length=1,choices=LEVEL_USER,default='l')