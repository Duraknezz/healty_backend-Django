from django.db import models
from citas.models import Cita

class RegistroDiario(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField()


    comida = models.TextField(null=True, blank=True)       
    hora = models.TimeField(null=True, blank=True)          
    porciones = models.IntegerField(null=True, blank=True)  
    calorias_consumidas = models.IntegerField(null=True, blank=True)
    agua_ml = models.IntegerField(null=True, blank=True)    
    estado = models.CharField(max_length=255, null=True, blank=True)  

    cumplio = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.cita} - {self.fecha}"
