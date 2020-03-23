from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    name = models.TextField(null=False)
    number = models.TextField(null=False)
    photo = models.TextField(null=True)
    favorite = models.BooleanField(null=False)
    deleted = models.BooleanField(null=False)

    # def __str__(self):
    #     return self.name
