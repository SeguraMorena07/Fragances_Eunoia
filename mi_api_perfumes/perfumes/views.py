from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Perfume, Marca
from .serializer import PerfumeSerializer, MarcaSerializer # Asegúrate de que este archivo exista

class PerfumeViewSet(viewsets.ModelViewSet):
    """Viewset que maneja las operaciones CRUD para el modelo Perfume."""
    permission_classes = [IsAuthenticated]
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    """Viewset que maneja las operaciones CRUD para el modelo Marca."""
    permission_classes = [IsAuthenticated]
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

