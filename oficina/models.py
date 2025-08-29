from django.db import models
from django.core.exceptions import ValidationError

def validate_nombre_corto(value):
    if not value.isupper():
        raise ValidationError(
            f'{value} debe estar en mayusculas'
        )
# Create your models here.
class Oficina(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la oficina',max_length=100,unique=True)
    nombre_corto = models.SlugField(verbose_name='id corto',max_length=10, unique=True, help_text='Identificador unico de la oficina')
    validators = [validate_nombre_corto]
    class Meta:
        verbose_name = 'oficina'
        verbose_name_plural = 'oficinas'

    def __str__(self):
        return f'{self.nombre}-{self.nombre_corto}'
    