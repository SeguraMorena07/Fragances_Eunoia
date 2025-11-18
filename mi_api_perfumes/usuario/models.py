from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Hereda todos los campos de AbstractUser (username, email, password, etc.)
    # Puedes añadir campos personalizados aquí si lo deseas (ej: direccion, telefono)
    pass

