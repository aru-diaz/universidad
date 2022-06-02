from django.contrib import admin
from .models import Materia, Alumno, Docente, Grupo, GrupoMateria
# Register your models here.
admin.site.register(Materia)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(GrupoMateria)
