from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True, blank=False, null=False)
    is_admin = models.BooleanField(default= False)
    is_verified = models.BooleanField(default = False)

    def __str__(self):
        return self.username
    
