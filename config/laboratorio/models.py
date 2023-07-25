# laboratorio/models.py
from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='Concepcion')  # Nuevo campo: ciudad
    pais = models.CharField(max_length=100, default='Chile') 

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default='Medicina general') 

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(verbose_name='Fecha de fabricación', null=True, blank=True)
    p_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de costo')
    p_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de venta')

    class Meta:
        # Restricción: Un producto solo puede pertenecer a un solo laboratorio
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'laboratorio'], name='producto_unico_laboratorio')
        ]

    def __str__(self):
        return self.nombre
