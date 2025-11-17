from rest_framework import viewsets
from .models import Perfume, Marca
from .serializer import PerfumeSerializer, MarcaSerializer # Asegúrate de que este archivo exista

class PerfumeViewSet(viewsets.ModelViewSet):
    """Viewset que maneja las operaciones CRUD para el modelo Perfume."""
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    """Viewset que maneja las operaciones CRUD para el modelo Marca."""
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

