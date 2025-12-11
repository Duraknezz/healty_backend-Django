from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cita
from .serializers import CitaSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        # Filtro por paciente
        paciente_id = params.get("paciente")
        if paciente_id:
            qs = qs.filter(paciente_id=paciente_id)

        # Filtro por tipo
        tipo = params.get("tipo")
        if tipo:
            qs = qs.filter(tipo=tipo)

        # Filtro por fecha mínima
        fecha_inicio = params.get("fecha_inicio")
        if fecha_inicio:
            qs = qs.filter(fecha__gte=fecha_inicio)

        # Filtro por fecha máxima
        fecha_fin = params.get("fecha_fin")
        if fecha_fin:
            qs = qs.filter(fecha__lte=fecha_fin)

        # Filtro general por texto (motivo)
        search = params.get("search")
        if search:
            qs = qs.filter(motivo__icontains=search)

        # Orden final
        return qs.order_by("-fecha", "-hora")
