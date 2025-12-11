from django.contrib import admin

# Register your models here.
from .models import Paciente  # Asegúrate de que el nombre del modelo sea correcto

# Registra tu modelo en el sitio de administración
admin.site.register(Paciente)