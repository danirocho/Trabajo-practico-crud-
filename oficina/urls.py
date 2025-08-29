from django.urls import path
from .views import *

app_name = 'oficina'
urlpatterns = [
    path(
        'lista_oficina/', OficinaListView.as_view(),
        name='lista_oficina'),
    path(
        'detalle/<int:pk>/', OficinaDetailView.as_view(),
        name='detalle_oficina'),
    path(
        'crear/', OficinaCreateView.as_view(),
        name='crear_oficina'),
    path(
        'editar/<int:pk>/', OficinaUpdateView.as_view(),
        name='editar_oficina'),
    path(
        'eliminar/<int:pk>/', OficinaDeleteView.as_view(),
        name='eliminar_oficina'),
    path(
        'buscar/', OficinaSearchView.as_view(),
        name='buscar_oficina'),

]