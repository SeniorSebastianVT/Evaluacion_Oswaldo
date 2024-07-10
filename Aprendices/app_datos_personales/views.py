from django.shortcuts import render, redirect
from app_datos_personales.models import Aprendiz
from django.http import HttpResponse
from .forms import AprendizForm


# Create your views here.
def base(request):
  return render(request, 'app_datos_personales/base.html')



# Create your views here.

def inicio(request):
    return render(request, 'D:/Evaluacion_Oswaldo/Aprendices/app_datos_personales/templates/app_datos_personales/inicio.html')

def hola(request):
    return render(request, 'D:/Evaluacion_Oswaldo/Aprendices/app_datos_personales/templates/app_datos_personales/hola.html')

def aprendices(request):
    aprendices = Aprendiz.objects.all()
    return render(request, "aprendices.html",{"aprendices": aprendices})

def crear_aprendiz(request):
    formulario = AprendizForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('aprendices')
    return render(request, "crear_aprendiz.html", {'formulario': formulario})

def editar_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id_aprendiz=id_aprendiz)
    formulario = AprendizForm(request.POST or None, instance=aprendiz)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('aprendices')
    return render(request, "editar_aprendiz.html", {'formulario': formulario})

def eliminar_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id_aprendiz=id_aprendiz)
    aprendiz.delete()
    return redirect('aprendices')



