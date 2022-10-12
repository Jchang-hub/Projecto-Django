from django.shortcuts import render, redirect
from .models import Persona, Pais
from .forms import PersonaForm
from django.http import JsonResponse
import json


# Create your views here.
def json(request):
    data = list(Pais.objects.values())
    return JsonResponse(data, safe=False)

def home(request):
    personas = Persona.objects.all()
    return render(request, 'paginas/home.html', {'personas':personas})

def consulta(request, id):
    persona = Persona.objects.get(id=id)
    formulario = PersonaForm(request.POST or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('home')
    return render(request, 'paginas/consulta.html',{'formulario':formulario})

def nuevo(request):
    formulario = PersonaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')
    return render(request, 'paginas/nuevo.html',{'formulario':formulario})
