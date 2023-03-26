from collections import defaultdict
from django.shortcuts import render, HttpResponse
from .models import*
# Create your views here.
def index (request):

    varEstudiante= Estudiante.objects.filter(grupo=1)
    varEstudiante2=Estudiante.objects.filter(grupo=4)
    #mostrar los alumnos con el mismo apellido 
    varApellido = Estudiante.objects.filter(apellidos="Mendoza")
    varApellido2 = Estudiante.objects.filter(apellidos="Landaverde")
    varApellido3 = Estudiante.objects.filter(apellidos="Garces")
    varApellido4 = Estudiante.objects.filter(apellidos="Gómez")
    ap=Estudiante.objects.values_list('apellidos',flat=True)
    estudianteapellido=defaultdict(list)
    for estudiante in Estudiante.objects.all():
        estudianteapellido[estudiante.apellidos].append(estudiante.nombres)
        mismoapellido=[]
    for apellidos, estudiantes in estudianteapellido.items():
        if len(estudiantes)>1:
            mismoapellido.append({'apellidos':apellidos,'estudiantes':estudiantes})

    #muestra los alumnos que tiene  la misma edad 
    ed=Estudiante.objects.values_list('edad',flat=True)
    estudianteporedad=defaultdict(list)
    for estudiante in Estudiante.objects.all():
        estudianteporedad[estudiante.edad].append(estudiante.nombres)
        mismaedad=[]
    for edad, estudiantes in estudianteporedad.items():
        if len(estudiantes)>1:
            mismaedad.append({'edad':edad,'estudiantes':estudiantes})
    # muestra el grupo 3 y los que tienen la misma edad 
    varEstudiante3=Estudiante.objects.filter(grupo=3, edad=22 )
    
    varTodosEstudiantes= Estudiante.objects.all()

    return render (request, 'index.html',{'varEstudiante':varEstudiante,'varEstudiante2':varEstudiante2,'varApellido': varApellido,'varApellido2': varApellido2,'varApellido3': varApellido3,'varApellido4': varApellido4,  'varTodosEstudiantes':varTodosEstudiantes,'mismaedad':mismaedad, 'varEstudiante3': varEstudiante3,'mismoapellido':mismoapellido})