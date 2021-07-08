from django.contrib import admin
from .models import Servicio, Proveedor
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display =["servicio_id","nombre"]
    list_editable=["nombre"]
    search_fields=["nombre"]

class ProveedorAdmin(admin.ModelAdmin):
    list_display =["rut","nombre","servicio", "descripcion","telefono", "email"]
    search_fields=["nombre"]
    list_filter = ["nombre","servicio"]
    list_per_page = 8


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Proveedor, ProveedorAdmin )