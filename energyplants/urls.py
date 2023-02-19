from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CombustibleCreateView, TipoPlantaCreateView, PlantaCreateView, LugarCreateView

router = DefaultRouter()
router.register('combustible', CombustibleCreateView)
router.register('planta', PlantaCreateView)
router.register('tipoplanta', TipoPlantaCreateView)
router.register('lugar', LugarCreateView)


urlpatterns = [    
    path('', include(router.urls)),
    path('tipoplanta/renovables/contador', TipoPlantaCreateView.ContadorPlantasRenovables, name='contador'),  
]