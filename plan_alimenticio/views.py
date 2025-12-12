from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PlanAlimenticio
from .serializers import PlanAlimenticioSerializer

class PlanAlimenticioViewSet(viewsets.ModelViewSet):
    queryset = PlanAlimenticio.objects.all()
    serializer_class = PlanAlimenticioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        # filtrar por cita
        cita_id = params.get("cita")
        if cita_id:
            qs = qs.filter(cita_id=cita_id)

        # filtro por fecha
        fecha = params.get("fecha")
        if fecha:
            qs = qs.filter(fecha=fecha)

        # búsqueda en motivo o recomendaciones
        search = params.get("search")
        if search:
            qs = qs.filter(
                models.Q(motivo__icontains=search) |
                models.Q(recomendaciones__icontains=search)
            )

        return qs
