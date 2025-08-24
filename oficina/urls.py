from django.urls import path
from . import views

app_name = 'oficina'
urlpatterns = [
    path(
        'lista/', views.OficinaListView.as_view(),
        name='lista_oficina'),
    path(
        'detalle/<int:pk>/', views.OficinaDetailView.as_view(),
        name='detalle_oficina'),
    path(
        'crear/', views.OficinaCreateView.as_view(),
        name='crear_oficina'),
    path(
        'editar/<int:pk>/', views.OficinaUpdateView.as_view(),
        name='editar_oficina'),
    path(
        'eliminar/<int:pk>/', views.OficinaDeleteView.as_view(),
        name='eliminar_oficina'),
    path(
        'buscar/', views.OficinaSearchView.as_view(),
        name='buscar_oficina'),

]