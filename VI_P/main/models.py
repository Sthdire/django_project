from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, UserManager
)
class Model(models.Model):
    email = models.CharField(max_length=50, unique=True)