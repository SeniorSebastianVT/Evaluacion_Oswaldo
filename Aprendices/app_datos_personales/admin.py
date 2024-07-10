from django.contrib import admin
from app_datos_personales.models import Aprendiz

# Register your models here.

class AprendizAdmin(admin.ModelAdmin):
    readonly_charset=("created","updated")

admin.site.register(Aprendiz,AprendizAdmin)