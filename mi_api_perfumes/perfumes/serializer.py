from rest_framework import serializers
from .models import Marca, Perfume, Carrito, ItemCarrito, Pedido, Stock

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

class ItemCarritoSerializer(serializers.ModelSerializer):
    nombre_perfume = serializers.ReadOnlyField(source='perfume.nombre')

    class Meta:
        model = ItemCarrito
        fields = ['id', 'perfume', 'nombre_perfume', 'cantidad', 'carrito']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(source='itemcarrito_set', many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'items'] 

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    nombre_perfume = serializers.ReadOnlyField(source='perfume.nombre')
    
    class Meta:
        model = Stock
        fields = ['id', 'perfume', 'nombre_perfume', 'cantidad_disponible']

