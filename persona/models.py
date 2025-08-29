from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    """Model definition for MODELNAME."""

    nombre = models.CharField(verbose_name='Nombre completo', max_length=50)
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    edad = models.IntegerField(verbose_name='Edad')
    oficina = models.ForeignKey(
        Oficina,
        verbose_name='Oficina asignada',
         on_delete=models.PROTECT,
          related_name='personas',
           null=True, blank=True)
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'PERSONA'
        verbose_name_plural = 'personas'

    def __str__(self):
        """Unicode representation of persona."""
        return f'{self.nombre} - {self.apellido}' + f' - {self.edad} años'

