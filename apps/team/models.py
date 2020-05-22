from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Alumnos:
    nombre/apellidos
    expediente
    grupo
    semestre
    carrera

    liberado
    fecha de inscripción

team:
    deporte
    docente o cargo
    máximo de alumnos
    horario
    lugar
"""

class Student(models.Model):
    name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    group = models.IntegerField()
    semestre = models.IntegerField()
    carrera = models.CharField(max_length=5)
    liberado = models.BooleanField(default=False)
    date_enrollment = models.DateTimeField(auto_now=True)

class Team(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.CharField(max_length=25)
    max_students = models.IntegerField()
    schedule = models.CharField(max_length=50)
    place = models.CharField(max_length=25)

