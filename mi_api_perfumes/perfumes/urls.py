from rest_framework.routers import DefaultRouter
from .views import ( 
    PerfumeViewSet, MarcaViewSet, CarritoViewSet, ItemCarritoViewSet, 
    PedidoViewSet, StockViewSet
)

router = DefaultRouter()


router.register(r'perfumes', PerfumeViewSet) 
router.register(r'marcas', MarcaViewSet)
router.register(r'carritos', CarritoViewSet, basename='carrito')
router.register(r'items', ItemCarritoViewSet, basename='itemcarrito')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'stock', StockViewSet, basename='stock')

urlpatterns = router.urls