from rest_framework import serializers
from .models import PlanAlimenticio

class PlanAlimenticioSerializer(serializers.ModelSerializer):
    cita_id = serializers.IntegerField(source="cita.id", read_only=True)
    paciente_id = serializers.IntegerField(source="cita.paciente.id", read_only=True)
    paciente_nombre = serializers.CharField(source="cita.paciente.nombre", read_only=True)
    paciente_apellido = serializers.CharField(source="cita.paciente.apellido", read_only=True)

    class Meta:
        model = PlanAlimenticio
        fields = "__all__"
