from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Team
from .models import Student
from .forms import  StudentForm

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

def team_details(request, team_id):
    #Vista de registro de un alumno a un taller
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_details', team_id)
        team = Team.objects.get(pk=team_id)
        students = Student.objects.filter(team_id = team_id)
        return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
    team = Team.objects.get(pk=team_id)
    students = Student.objects.filter(team_id = team_id)
    form = StudentForm(initial={'team':team_id})
    return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})


