from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from personas.models import Persona

def bienvenido(consulta):
    nro_personas = Persona.objects.count()
    personas = Persona.objects.all()
    #mensajes = {'msj1': 'valor mensaje 1', 'msj2': 'valor mensaje 2'}
    return render(consulta, 'bienvenido.html', {'nro_personas': nro_personas, 'personas': personas}) #<- mensajes

def despedirse(consulta):
    return HttpResponse("despedida de Django")

def contactar(consulta):
    return HttpResponse('Contacto: +591 798955')