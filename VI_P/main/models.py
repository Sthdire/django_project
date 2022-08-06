from django.db import models


class UserReg(models.Model):
    username = models.CharField('username', max_length=20, unique=True)
    password = models.CharField('password', max_length=20)

    def __unicode__(self):
        return self.username
