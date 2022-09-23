from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(consulta):
    return HttpResponse('Hola mundo desde django')

def despedirse(consulta):
    return HttpResponse("despedida de Django")

def contactar(consulta):
    return HttpResponse('Contacto: +591 798955')