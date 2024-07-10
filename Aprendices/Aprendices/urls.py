from django.contrib import admin
from django.urls import path
from app_datos_personales.views import base,hola, inicio, aprendices, crear_aprendiz, editar_aprendiz, eliminar_aprendiz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base),
    path('', inicio, name='inicio'),
    path('hola/', hola, name= 'hola'),

    path('aprendices/', aprendices, name="aprendices"),
    path('crear_aprendiz/', crear_aprendiz, name="crear_aprendiz"),
    path('editar_aprendiz/', editar_aprendiz, name="editar_aprendiz"),
    path('eliminar_aprendiz/<int:id_aprendiz>', eliminar_aprendiz, name="eliminar_aprendiz"),
    path('editar_aprendiz/<int:id_aprendiz>', editar_aprendiz, name="editar_aprendiz"),
    
]