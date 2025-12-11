from rest_framework import serializers
from .models import Cita

class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(source="paciente.nombre", read_only=True)

    class Meta:
        model = Cita
        fields = [
            "id",
            "paciente",
            "paciente_nombre",
            "fecha",
            "hora",
            "motivo",
            "tipo",
            "estado",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]