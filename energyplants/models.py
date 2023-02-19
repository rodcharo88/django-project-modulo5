from django.db import models
from .validators import validate_min_max_value, validate_positive_value
#TextChoices
class UnidadesCapacidad(models.TextChoices):
    KILOWATTS = 'KW', 'Kilowatts'
    MEGAWATTS = 'MW', 'Megawatts',
    MMBTUHORA = 'MMBTU/hr', 'Millon de BTU/Hora',

class UnidadesCostoCombustible(models.TextChoices):
    USDMEGAWATTSHORA = '$/MWh', 'Dolares por Megawatts-hora',
    USDMMBTU = '$/MMBTU', 'Dolares por Millon de BTU',

#Models
class Combustible(models.Model):
    combustible = models.CharField(max_length=100, unique=True)
    costo = models.DecimalField(decimal_places=4, max_digits=10, validators=[validate_positive_value])
    unidades = models.CharField(
        max_length=7,
        choices=UnidadesCostoCombustible.choices,
        default=UnidadesCostoCombustible.USDMEGAWATTSHORA,
        )
    def __str__(self):
        return self.combustible 
        
class Lugar(models.Model):
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    canton = models.CharField(max_length=100)
    def __str__(self):
        return self.canton 

class TipoPlanta(models.Model):
    tipo = models.CharField(max_length=100)
    tipogen = models.CharField(max_length=100)
    renovable = models.BooleanField(default=False)
    combustible = models.ForeignKey(Combustible, on_delete= models.RESTRICT, null=True)
    eficiencia = models.PositiveSmallIntegerField(validators=[validate_min_max_value])
    def __str__(self):
        return self.tipo 

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.DecimalField(decimal_places=5, max_digits=10, validators=[validate_positive_value])
    unidades = models.CharField(
        max_length=8,
        choices=UnidadesCapacidad.choices,
        default=UnidadesCapacidad.MEGAWATTS,
        )
    tipo = models.ForeignKey(TipoPlanta, on_delete= models.RESTRICT)
    lugar = models.ForeignKey(Lugar, on_delete= models.RESTRICT)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.nombre 