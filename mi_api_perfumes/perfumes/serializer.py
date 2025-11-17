from rest_framework import serializers
from .models import Marca, Perfume 

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class PerfumeSerializer(serializers.ModelSerializer):
    # Esto muestra el nombre de la marca en lugar de solo su ID
    marca_nombre = serializers.CharField(source='marca.nombre', read_only=True)
    
    class Meta:
        model = Perfume
        fields = ['id', 'nombre', 'marca', 'marca_nombre', 'precio', 'descripcion']

