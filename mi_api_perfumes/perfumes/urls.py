from rest_framework.routers import DefaultRouter
from .views import PerfumeViewSet, MarcaViewSet # <-- Importación directa

router = DefaultRouter()

# Ya no necesitas 'views.' porque las importaste directamente
router.register(r'perfumes', PerfumeViewSet) 
router.register(r'marcas', MarcaViewSet)

urlpatterns = router.urls

