from django.db import models
from citas.models import Cita  

class PlanAlimenticio(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='planes')
    fecha = models.DateField(auto_now_add=False)
    hora = models.TimeField(auto_now=False, null=True, blank=True)
    motivo = models.CharField(max_length=255, blank=True)
    calorias = models.IntegerField(null=True, blank=True)
    proteina_g = models.IntegerField(null=True, blank=True)
    carbohidratos_g = models.IntegerField(null=True, blank=True)
    grasas_g = models.IntegerField(null=True, blank=True)
    verduras = models.CharField(max_length=255, blank=True)
    frutas = models.CharField(max_length=255, blank=True)
    recomendaciones = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-hora', '-created_at']

    def __str__(self):
        return f'Plan {self.id} - Cita {self.cita_id} - {self.fecha}'
