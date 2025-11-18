from rest_framework import viewsets
from .permissions import ReadOnlyIfUnauthenticated
from rest_framework.permissions import IsAuthenticated
from .models import Perfume, Marca, Carrito, ItemCarrito, Pedido
from .serializer import PerfumeSerializer, MarcaSerializer, CarritoSerializer, ItemCarritoSerializer, PedidoSerializer 

class PerfumeViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyIfUnauthenticated]
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyIfUnauthenticated]
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CarritoSerializer

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)

class ItemCarritoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemCarritoSerializer

    def get_queryset(self):
        return ItemCarrito.objects.filter(carrito__usuario=self.request.user)

class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)
    
