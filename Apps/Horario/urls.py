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
    path('editarDocente/', views.editarDocente)
]
