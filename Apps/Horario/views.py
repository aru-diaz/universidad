from django.shortcuts import render, redirect
from .models import Materia, Docente, Grupo, Alumno, GrupoMateria, GrupoMateria
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def salir(request):
    logout(request)
    return redirect('/')

@login_required
def inicio(request):    
    return render(request, "inicio.html")

@login_required
def materias(request):
    materias = Materia.objects.all()
    return render(request, "materias/gestionMaterias.html", {"materias":materias})

@login_required
def registrarMateria(request):
    idMateria = request.POST['idMateria']
    nombreMateria = request.POST['nombreMateria']
    creditosMateria = request.POST['creditosMateria']
    try:
        materia = Materia.objects.create(
            idMateria=idMateria, nombreMateria=nombreMateria, creditosMateria=creditosMateria)
        messages.success(request, '¡Materia registrada!')
    except IntegrityError:
        messages.success(request, '¡Materia NO registrada, duplicado de id!')
        return redirect('/materias')        

    return redirect('/materias')

@login_required
def eliminarMateria(request, idMateria):
    materia = Materia.objects.get(idMateria=idMateria)
    materia.delete()

    messages.success(request, '¡Materia eliminada!')
    return redirect('/materias')

@login_required
def edicionMateria(request, idMateria):
    materia = Materia.objects.get(idMateria=idMateria)
    return render(request, "materias/edicionMaterias.html", {"materia": materia})

@login_required
def editarMateria(request):
    idMateria = request.POST['idMateria']
    nombreMateria = request.POST['nombreMateria']
    creditosMateria = request.POST['creditosMateria']
    try:
        materia = Materia.objects.get(idMateria=idMateria)
        materia.nombreMateria = nombreMateria
        materia.creditosMateria = creditosMateria
        materia.save()
        messages.success(request, '¡Materia actualizada!')
    except IntegrityError:
        messages.success(request, '¡La materia no se pudo editar!')
        return redirect('/materias')     
    return redirect('/materias')

##################################################################

@login_required
def docentes(request):
    docentes = Docente.objects.all()
    return render(request, "docentes/gestionDocentes.html", {"docentes":docentes})

@login_required
def registrarDocente(request):
    idDocente = request.POST['idDocente']
    nombreDocente = request.POST['nombreDocente']
    apellidoDocente = request.POST['apellidoDocente']

    try:
        docente = Docente.objects.create(
            idDocente=idDocente, nombreDocente=nombreDocente, apellidoDocente=apellidoDocente)
        messages.success(request, '¡Docente registrado!')
    except IntegrityError:
        messages.success(request, '¡Docente NO registrado, duplicado de id!')
        return redirect('/docentes')
    return redirect('/docentes')

@login_required
def eliminarDocente(request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    docente.delete()
    messages.success(request, '¡Docente eliminado!')
    return redirect('/docentes')

@login_required
def edicionDocente(request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    return render(request, "docentes/edicionDocentes.html", {"docente": docente})

@login_required
def editarDocente(request):
    idDocente = request.POST['idDocente']
    nombreDocente = request.POST['nombreDocente']
    apellidoDocente = request.POST['apellidoDocente']
    try:
        docente = Docente.objects.get(idDocente=idDocente)
        docente.nombreDocente = nombreDocente
        docente.apellidoDocente = apellidoDocente
        docente.save()
        messages.success(request, '¡Docente actualizado!')
    except IntegrityError:
        messages.success(request, '¡El docente no se pudo editar!')
        return redirect('/docentes')         

    return redirect('/docentes')

####################################################################################

@login_required
def grupos(request):
    grupos = Grupo.objects.all()
    docentes = Docente.objects.all()
    return render(request, "grupos/gestionGrupos.html", {"grupos":grupos,"docentes":docentes})

@login_required
def registrarGrupo(request):
    idGrupo = request.POST['idGrupo']
    nombreGrupo = request.POST['nombreGrupo']
    idDocente = request.POST['idDocente']

    try:
        grupo = Grupo.objects.create(
            idGrupo=idGrupo, nombreGrupo=nombreGrupo, idDocente=Docente.objects.get(idDocente=idDocente))
        messages.success(request, '¡Grupo registrado!')
    except IntegrityError:
        messages.success(request, '¡Grupo NO registrado!, duplicado de id o duplicado de docente!')
        return redirect('/grupos')
    return redirect('/grupos')

@login_required
def eliminarGrupo(request, idGrupo):
    grupo = Grupo.objects.get(idGrupo=idGrupo)
    grupo.delete()
    messages.success(request, '¡Grupo eliminado!')
    return redirect('/grupos')

@login_required
def edicionGrupo(request, idGrupo):
    grupo = Grupo.objects.get(idGrupo=idGrupo)
    docentes = Docente.objects.all()
    return render(request, "grupos/edicionGrupos.html", {"grupo": grupo, "docentes":docentes})

@login_required
def editarGrupo(request):
    idGrupo = request.POST['idGrupo']
    nombreGrupo = request.POST['nombreGrupo']
    idDocente = request.POST['idDocente']

    try:
        grupo = Grupo.objects.get(idGrupo=idGrupo)
        grupo.nombreGrupo = nombreGrupo
        grupo.idDocente = Docente.objects.get(idDocente=idDocente)
        grupo.save()
        messages.success(request, '¡Grupo actualizado!')
    except IntegrityError:
        messages.success(request, '¡El grupo no se pudo editar!')
        return redirect('/grupos')          

    return redirect('/grupos')

@login_required
def detalleGrupo(request, idGrupo):
    grupo = Grupo.objects.get(idGrupo=idGrupo)    
    alumnos = Alumno.objects.filter(idGrupo=idGrupo)
    materias = Materia.objects.all()
    grupoMaterias = GrupoMateria.objects.filter(idGrupo=idGrupo)
    contador = GrupoMateria.objects.filter(idGrupo=idGrupo).count()
    return render(request, "grupos/detalleGrupo.html", {"grupo":grupo,"alumnos":alumnos,"materias":materias,"grupoMaterias":grupoMaterias,"contador":contador})

@login_required
def registrarGrupoMateria(request, idGrupo):
    idMateria = request.POST['idMateria']
    idGrupo = idGrupo

    try:
        grupoMateria = GrupoMateria.objects.create(
            idGrupo=Grupo.objects.get(idGrupo=idGrupo),idMateria=Materia.objects.get(idMateria=idMateria))
        messages.success(request, '¡Materia registrada!')
    except IntegrityError:
        messages.success(request, 'Materia NO registrada!, duplicado de materia en el grupo!')
        return redirect('../detalleGrupo/'+idGrupo)
    return redirect('../detalleGrupo/'+idGrupo)

@login_required
def eliminarGrupoMateria(request, idGrupo, idMateria):
    grupoMateria = GrupoMateria.objects.get(idGrupo=Grupo.objects.get(idGrupo=idGrupo),idMateria=Materia.objects.get(idMateria=idMateria))
    grupoMateria.delete()
    messages.success(request, '¡Materia eliminada eliminado!')
    return redirect('../../detalleGrupo/'+idGrupo)
####################################################################################

@login_required
def alumnos(request):
    alumnos = Alumno.objects.all()
    grupos = Grupo.objects.all()    
    return render(request, "alumnos/gestionAlumnos.html", {"alumnos":alumnos, "grupos":grupos})

@login_required
def registrarAlumno(request):
    idAlumno = request.POST['idAlumno']
    nombreAlumno = request.POST['nombreAlumno']
    apellidoAlumno = request.POST['apellidoAlumno']
    idGrupo = request.POST['idGrupo']

    try:
        alumno = Alumno.objects.create(
            idAlumno=idAlumno, nombreAlumno=nombreAlumno, apellidoAlumno=apellidoAlumno, idGrupo=Grupo.objects.get(idGrupo=idGrupo))
        messages.success(request, '¡Alumno registrado!')
    except IntegrityError:
        messages.success(request, '¡Alumno NO registrado!, duplicado de id!')
        return redirect('/alumnos')
    return redirect('/alumnos')

@login_required
def eliminarAlumno(request, idAlumno):
    alumno = Alumno.objects.get(idAlumno=idAlumno)
    alumno.delete()
    messages.success(request, '¡Alumno eliminado!')
    return redirect('/alumnos')

@login_required
def edicionAlumno(request, idAlumno):
    alumno = Alumno.objects.get(idAlumno=idAlumno)
    grupos = Grupo.objects.all()
    return render(request, "alumnos/edicionAlumnos.html", {"alumno": alumno, "grupos": grupos})

@login_required
def editarAlumno(request):
    idAlumno = request.POST['idAlumno']
    nombreAlumno = request.POST['nombreAlumno']
    apellidoAlumno = request.POST['apellidoAlumno']
    idGrupo = request.POST['idGrupo']

    try:
        alumno = Alumno.objects.get(idAlumno=idAlumno)
        alumno.nombreAlumno = nombreAlumno
        alumno.apellidoAlumno = apellidoAlumno
        alumno.idGrupo = Grupo.objects.get(idGrupo=idGrupo)
        alumno.save()
        messages.success(request, '¡Alumno actualizado!')
    except IntegrityError:
        messages.success(request, '¡El alumno no se pudo editar!')
        return redirect('/alumnos')          

    return redirect('/alumnos')

@login_required
def detalleAlumno(request, idAlumno, idGrupo):    
    alumno = Alumno.objects.get(idAlumno=idAlumno)
    grupoMaterias = GrupoMateria.objects.filter(idGrupo=Grupo.objects.get(idGrupo=idGrupo))    
    return render(request, "alumnos/detalleAlumno.html", {"alumno":alumno,"grupoMaterias":grupoMaterias})    