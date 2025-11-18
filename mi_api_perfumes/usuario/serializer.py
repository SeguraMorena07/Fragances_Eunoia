from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    # Campo 'password' escrito solo para escritura, nunca se muestra
    password = serializers.CharField(write_only=True)

    class Meta:
        # Usa el modelo de usuario personalizado
        model = User 
        # Campos que se envían en la solicitud de registro
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        # Llama al método de creación de usuario para hashear la contraseña
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
    
