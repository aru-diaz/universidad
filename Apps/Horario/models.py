from django.db import models

# Create your models here.
class Materia(models.Model):
    idMateria=models.CharField(primary_key=True,max_length=6)
    nombreMateria=models.CharField(max_length=50)
    creditosMateria=models.PositiveSmallIntegerField()

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombreMateria, self.creditosMateria)

class Docente(models.Model):
    idDocente=models.CharField(primary_key=True,max_length=6)
    nombreDocente=models.CharField(max_length=50)
    apellidoDocente=models.CharField(max_length=50)    

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.idDocente, self.nombreDocente)

class Grupo(models.Model):
    idGrupo=models.CharField(primary_key=True,max_length=6)
    nombreGrupo=models.CharField(max_length=50)
    idDocente=models.ForeignKey(Docente, on_delete=models.SET_NULL,null=True,default=0, unique=True)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.idGrupo, self.nombreGrupo)

class Alumno(models.Model):
    idAlumno=models.CharField(primary_key=True,max_length=6)
    nombreAlumno=models.CharField(max_length=50)
    apellidoAlumno=models.CharField(max_length=50)
    grupoAlumno=models.ForeignKey(Grupo, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.idAlumno, self.nombreAlumno)

class GrupoMateria(models.Model):
    class Meta:
        unique_together = (('idGrupo', 'idMateria'),)

    idGrupo=models.ForeignKey(Grupo, on_delete=models.CASCADE)
    idMateria=models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.idGrupo, self.idMateria)

