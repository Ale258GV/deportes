from django.urls import path
from . import views

urlpatterns = [
    # path('equipos/', views.equipos, name="equipos"),
    # path('estudiantes/', views.estudiantes, name="estudiantes"),
    # path('estudiantes/plan/<str:plan>/', views.estudiantes_plan, name="estudiantesByPlan"),
    # path('estudiantes/equipo/<int:id_equipo>/', views.estudiantes_equipo, name="estudiantesByTeam"),
    path('team_details/<int:team_id>/', views.team_details, name="team_details"),
    path('edit_team/<int:team_id>/', views.edit_team, name="edit_team"),
    path('delete_student/<int:student_id>/', views.delete_student, name="delete_student"),
    path('liberar_student/<int:student_id>/', views.liberar_student, name="liberar_student"),
    path('create_team/', views.create_team, name="create_team"),
]