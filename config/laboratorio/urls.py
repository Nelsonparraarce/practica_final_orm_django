# laboratorio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('laboratorio', views.mostrar_laboratorios, name='mostrar_laboratorios'),
    path('agregar-laboratorio/', views.agregar_laboratorio, name='agregar_laboratorio'),
    path('laboratorio/<int:laboratorio_id>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('laboratorio/<int:laboratorio_id>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
