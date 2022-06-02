from django.shortcuts import render, redirect
from .models import Materia, Docente
from django.db import IntegrityError

# Create your views here.
def inicio(request):    
    return render(request, "inicio.html")

def materias(request):
    materias = Materia.objects.all()
    return render(request, "materias/gestionMaterias.html", {"materias":materias})

def registrarMateria(request):
    idMateria = request.POST['idMateria']
    nombreMateria = request.POST['nombreMateria']
    creditosMateria = request.POST['creditosMateria']
    try:
        materia = Materia.objects.create(
            idMateria=idMateria, nombreMateria=nombreMateria, creditosMateria=creditosMateria)
    except IntegrityError:
        return redirect('/materias')

    return redirect('/materias')

def eliminarMateria(request, idMateria):
    materia = Materia.objects.get(idMateria=idMateria)
    materia.delete()

    return redirect('/materias')

def edicionMateria(request, idMateria):
    materia = Materia.objects.get(idMateria=idMateria)
    return render(request, "materias/edicionMaterias.html", {"materia": materia})

def editarMateria(request):
    idMateria = request.POST['idMateria']
    nombreMateria = request.POST['nombreMateria']
    creditosMateria = request.POST['creditosMateria']

    materia = Materia.objects.get(idMateria=idMateria)
    materia.nombreMateria = nombreMateria
    materia.creditosMateria = creditosMateria
    materia.save()

    return redirect('/materias')

##################################################################

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, "docentes/gestionDocentes.html", {"docentes":docentes})

def registrarDocente(request):
    idDocente = request.POST['idDocente']
    nombreDocente = request.POST['nombreDocente']
    apellidoDocente = request.POST['apellidoDocente']

    try:
        docente = Docente.objects.create(
            idDocente=idDocente, nombreDocente=nombreDocente, apellidoDocente=apellidoDocente)
    except IntegrityError:
        return redirect('/docentes')
    return redirect('/docentes')

def eliminarDocente(request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    docente.delete()

    return redirect('/docentes')

def edicionDocente(request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    return render(request, "docentes/edicionDocentes.html", {"docente": docente})

def editarDocente(request):
    idDocente = request.POST['idDocente']
    nombreDocente = request.POST['nombreDocente']
    apellidoDocente = request.POST['apellidoDocente']

    docente = Docente.objects.get(idDocente=idDocente)
    docente.nombreDocente = nombreDocente
    docente.apellidoDocente = apellidoDocente
    docente.save()

    return redirect('/docentes')