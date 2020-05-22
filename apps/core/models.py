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
    avatar = models.ImageField(upload_to='avatares/')
    descripcion = models.TextField()