from django.contrib import admin
from .models import Planta, TipoPlanta, Lugar, Combustible

class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'unidades', 'tipo', 'lugar',)
    ordering = ['capacidad']

class TipoPlantaAdmin(admin.ModelAdmin):
    list_display =('tipo', 'tipogen', 'renovable', 'combustible', 'eficiencia',)


admin.site.register(Planta, PlantaAdmin)
admin.site.register(TipoPlanta, TipoPlantaAdmin)
admin.site.register(Lugar)
admin.site.register(Combustible)
