from django.shortcuts import render

from personas.models import Persona

# Create your views here.

def detallePersona(consulta, id):
    persona = Persona.objects.get(pk=id)
    return render(consulta, 'personas/detalle.html', {'persona': persona})