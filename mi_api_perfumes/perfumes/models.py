from django.db import models
from usuario.models import User

class Marca(models.Model):
    """Modelo para representar la marca del perfume (e.g., Chanel, Dior)."""
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class Perfume(models.Model):
    """Modelo para representar un perfume individual."""
    nombre = models.CharField(max_length=200)
    # Relación uno a muchos: Un perfume pertenece a una sola marca.
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} de {self.marca.nombre}"


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        unique_together = ('carrito', 'perfume')

    def __str__(self):
        return f"{self.cantidad} x {self.perfume.nombre}"
    
ESTADOS_PEDIDO = (
    ('PENDIENTE', 'Pendiente de Pago'),
    ('PAGADO', 'Pago Confirmado'),
    ('ENVIADO', 'Enviado'),
    ('CANCELADO', 'Cancelado'),
)

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS_PEDIDO, default='PENDIENTE')
    direccion_envio = models.TextField()

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username}"
    
