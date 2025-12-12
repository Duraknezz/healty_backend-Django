from rest_framework.routers import DefaultRouter
from .views import PlanAlimenticioViewSet

router = DefaultRouter()
router.register(r'planes', PlanAlimenticioViewSet, basename='planes')

urlpatterns = router.urls
