from contextlib import redirect_stderr
from logging.config import valid_ident
from pyexpat import model
from urllib import request
from webbrowser import get
from django.shortcuts import render, get_object_or_404, redirect

from personas.models import Persona
from django.forms import modelform_factory

# Create your views here.

def detallePersona(consulta, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(consulta, 'personas/detalle.html', {'persona': persona})

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    #comprobamos si el metodo cambio a get de lado del frontend
    if request.method == 'POST':
        #guardar en la base de datos
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
        
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nueva_persona.html', {'formaPersona': formaPersona})