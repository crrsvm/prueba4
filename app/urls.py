from django.urls import path
from .views import index, contacto, formulario_enviado, seccion_gatos, seccion_perros, proveedores, agregar_proveedor,listar_proveedor,modificar_proveedor, eliminar_proveedor

urlpatterns = [
    path('', index, name="index" ),
    path('contacto/', contacto, name="contacto"),
    path('formulario_enviado/', formulario_enviado, name="formulario_enviado"),
    path('seccion_gatos/', seccion_gatos, name="seccion_gatos"),
    path('seccion_perros/', seccion_perros, name="seccion_perros"),
    path('proveedores/', proveedores, name="proveedores"),
    path('agregar_proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('listar_proveedor/', listar_proveedor, name="listar_proveedor"),
    path('modificar_proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminar_proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
]
