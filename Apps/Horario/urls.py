from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir',views.salir),
    path('',views.inicio),
    path('inicio',views.inicio),
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
    path('editarGrupo/', views.editarGrupo),
    path('detalleGrupo/<idGrupo>', views.detalleGrupo),
    path('registrarGrupoMateria/<idGrupo>', views.registrarGrupoMateria),
    path('eliminarGrupoMateria/<idGrupo>/<idMateria>', views.eliminarGrupoMateria),

    path('alumnos',views.alumnos),
    path('registrarAlumno/', views.registrarAlumno),
    path('eliminarAlumno/<idAlumno>', views.eliminarAlumno),
    path('edicionAlumno/<idAlumno>', views.edicionAlumno),
    path('editarAlumno/', views.editarAlumno),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
