from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Persona
from django.urls import reverse_lazy

class PersonaListView(ListView):
    model = Persona
    template_name = "persona/lista.html"
    context_object_name = "personas"

class PersonaDetailView(DetailView):
    model = Persona
    template_name = "persona/detalle.html"
    context_object_name = "persona"

class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/crear.html"
    fields = ['nombre','apellido', 'edad']
    success_url = reverse_lazy('persona:lista')

class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "persona/crear.html"
    fields = ['nombre','apellido', 'edad']
    success_url = reverse_lazy('persona:lista')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona/eliminar.html"
    success_url = reverse_lazy('persona:lista')

