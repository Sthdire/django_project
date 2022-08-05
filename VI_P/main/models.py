from django.contrib.auth.models import User
from django.db import models


class Organisation(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.PROTECT)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
