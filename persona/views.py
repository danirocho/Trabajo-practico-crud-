from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Persona
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from oficina.models import Oficina

class PersonaListView(ListView):
    model = Persona
    template_name = "persona/lista.html"
    context_object_name = "personas"
    paginate_by = 10

class PersonaDetailView(DetailView):
    model = Persona
    template_name = "persona/detalle.html"
    context_object_name = "persona"

class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    template_name = "persona/crear.html"
    fields = ['nombre','apellido', 'edad', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    template_name = "persona/editar.html"
    fields = ['nombre','apellido', 'edad', 'oficina']
    success_url = reverse_lazy('persona:lista')

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = "persona/eliminar.html"
    success_url = reverse_lazy('persona:lista')

class PersonaSearchView(ListView):
    model = Persona
    template_name = "persona/buscar.html"
    context_object_name = "personas"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Persona.objects.filter(nombre__icontains=query)
        return Persona.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Buscar Persona'
        context['query'] = self.request.GET.get("q", "")
        return context

