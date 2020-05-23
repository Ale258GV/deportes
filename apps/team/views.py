from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from .models import Student

# Create your views here.
def equipos(request):
    #Todos los equipos
    equipos = Team.objects.all()
    print("--------------------------")
    print(equipos)
    print("--------------------------")
    return HttpResponse(equipos)

def estudiantes(request):
    #Todos los estudiantes
    estudiantes = Student.objects.all()
    print("--------------------------")
    print(estudiantes)
    print("--------------------------")
    return HttpResponse(estudiantes)

def estudiantes_plan(request, plan):
    #estudiantes Plan
    estudiantes = Student.objects.filter(plan = plan)
    print("--------------------------")
    print(estudiantes)
    print("--------------------------")
    return HttpResponse(estudiantes)

def estudiantes_equipo(request, id_equipo):
    #estudiantes que pertenecen a un equipo
    estudiantes = Student.objects.filter(team_id = id_equipo)
    print("--------------------------")
    print(estudiantes)
    print("--------------------------")
    return HttpResponse(estudiantes)

