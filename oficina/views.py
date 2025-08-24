from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Oficina
from django.db.models import Q
# Create your views here.
class OficinaListView(ListView):
    model = Oficina
    template_name = 'oficina/lista_oficina.html'
    context_object_name = 'oficinas'
    paginate_by = 10

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = 'oficina/detalle_oficina.html'
    context_object_name = 'oficina'

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = 'oficina/crear_oficina.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:lista_oficina')

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = 'oficina/editar_oficina.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:lista_oficina')

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = 'oficina/eliminar_oficina.html'
    success_url = reverse_lazy('oficina:lista_oficina')

class OficinaSearchView(ListView):
    model = Oficina
    template_name = 'oficina/buscar_oficina.html'
    context_object_name = 'oficinas'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Oficina.objects.filter(
                Q(nombre__icontains=query) | Q(nombre_corto__icontains=query)
            )
        return Oficina.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context