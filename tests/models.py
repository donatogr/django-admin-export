# -- encoding: UTF-8 --
from django.db import models


class ModelUnderTest(models.Model):
    value = models.IntegerField(unique=True)
