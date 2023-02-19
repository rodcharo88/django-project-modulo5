from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Combustible, TipoPlanta, Planta, Lugar
from .serializers import CombustibleSerializer, TipoPlantaSerializer, PlantaSerializer, LugarSerializer
from django.http import JsonResponse

# Create your views here.
class CombustibleCreateView(viewsets.ModelViewSet):
    queryset = Combustible.objects.all()
    serializer_class = CombustibleSerializer
    
class TipoPlantaCreateView(viewsets.ModelViewSet):
    queryset = TipoPlanta.objects.all()
    serializer_class = TipoPlantaSerializer
    @api_view(["GET"])
    def ContadorPlantasRenovables(request):
        try:
            cantidad = TipoPlanta.objects.filter(renovable=True).count()
            return JsonResponse(
                {"renovable": cantidad},
                safe=False,
                status=200,
            ) 
        except Exception as e:
            return JsonResponse({"mensaje": str(e)}, status=400)

class PlantaCreateView(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class LugarCreateView(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer



