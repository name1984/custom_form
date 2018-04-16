# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

#Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# Create your models here.
class ExtraInfo(models.Model):
    """
    This model contains one extra field cedula that will be saved  when a user registers.
     The form that wraps this model in in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)

    cedula = models.CharField(
        verbose_name = "CEDULA DE CIUDADANIA",
        max_length=10,
    )