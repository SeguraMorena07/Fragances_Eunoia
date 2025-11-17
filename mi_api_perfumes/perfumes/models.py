from django.db import models

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
    

