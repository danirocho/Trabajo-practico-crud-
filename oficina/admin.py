from django.contrib import admin
from .models import Oficina
admin.site.register(Oficina)

# Register your models here.
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto')
    search_fields = ('nombre', 'nombre_corto')