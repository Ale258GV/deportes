from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
Docente:
    Foto
    Descripción
"""
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user, self.description)