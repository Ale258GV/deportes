from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Team
from .models import Student
from .forms import StudentForm, TeamForm

# Create your views here.
# def equipos(request):
#     #Todos los equipos
#     equipos = Team.objects.all()
#     print("--------------------------")
#     print(equipos)
#     print("--------------------------")
#     return HttpResponse(equipos)

# def estudiantes(request):
#     #Todos los estudiantes
#     estudiantes = Student.objects.all()
#     print("--------------------------")
#     print(estudiantes)
#     print("--------------------------")
#     return HttpResponse(estudiantes)

# def estudiantes_plan(request, plan):
#     #estudiantes Plan
#     estudiantes = Student.objects.filter(plan = plan)
#     print("--------------------------")
#     print(estudiantes)
#     print("--------------------------")
#     return HttpResponse(estudiantes)

# def estudiantes_equipo(request, id_equipo):
    #estudiantes que pertenecen a un equipo
    # estudiantes = Student.objects.filter(team_id = id_equipo)
    # print("--------------------------")
    # print(estudiantes)
    # print("--------------------------")
    # return HttpResponse(estudiantes)

@login_required
def team_details(request, team_id):
    #Vista de registro de un alumno a un taller
    team = get_object_or_404(Team, pk=team_id)
    students = Student.objects.filter(team_id = team_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        total_students = Student.objects.filter(team_id = team_id).count()
        if total_students < team.max_students:
            if form.is_valid():
                form.save()
                messages.success(request, 'Listo')
                return redirect('team_details', team_id)
            return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
        else:
            messages.error(request, 'Cupo lleno')
        return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
    form = StudentForm(initial={'team':team_id})
    return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})

@login_required
def edit_team(request, team_id):
    #team = Team.objects.get(pk=team_id)
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, 'Listo, cambios guardados.')
        else:
            messages.error(request, 'Faltan Datos')
    form = TeamForm(instance=team)
    return render(request, 'edit_team.html', {'form':form})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    team_id = student.team.id
    student.delete()
    return redirect('team_details', team_id)

@login_required
def liberar_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.liberado = True
    team_id = student.team.id
    student.save()
    return redirect('team_details', team_id)

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='panel')
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo registrar, revisa tus datos')
    form = TeamForm()
    return render(request, 'create_team.html', {'form':form})