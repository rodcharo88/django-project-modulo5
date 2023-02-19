from django.core.exceptions import ValidationError

#Validations
def validate_min_max_value(value):
    if (value <= 0 or value >= 100):
        raise ValidationError('El valor debe ser un número entre 0 y 100')

def validate_positive_value(value):
    if(value < 0):
        raise ValidationError('El valor debe ser un número positivo')
