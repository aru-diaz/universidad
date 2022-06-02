from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio),
    path('materias',views.materias),
    path('registrarMateria/', views.registrarMateria),
    path('eliminarMateria/<idMateria>', views.eliminarMateria),
    path('edicionMateria/<idMateria>', views.edicionMateria),
    path('editarMateria/', views.editarMateria),

    path('docentes',views.docentes),
    path('registrarDocente/', views.registrarDocente),
    path('eliminarDocente/<idDocente>', views.eliminarDocente),
    path('edicionDocente/<idDocente>', views.edicionDocente),
    path('editarDocente/', views.editarDocente),

    path('grupos',views.grupos),
    path('registrarGrupo/', views.registrarGrupo),
    path('eliminarGrupo/<idGrupo>', views.eliminarGrupo),
    path('edicionGrupo/<idGrupo>', views.edicionGrupo),
    path('editarGrupo/', views.editarGrupo)
]
