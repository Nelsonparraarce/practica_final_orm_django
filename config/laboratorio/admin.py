from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','ciudad','pais')

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','laboratorio','especialidad')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'year_fabricacion', 'p_venta', 'p_costo')

    def year_fabricacion(self, obj):
        return obj.f_fabricacion.year if obj.f_fabricacion else None

    year_fabricacion.short_description = 'Año de fabricación'
    year_fabricacion.admin_order_field = 'f_fabricacion'