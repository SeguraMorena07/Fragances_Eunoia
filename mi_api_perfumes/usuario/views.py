from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializer import UserRegisterSerializer # Asegúrate de que este serializer exista

class RegisterView(APIView):
    # Permite acceso sin autenticación para registrar
    permission_classes = [] 
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "Registro exitoso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [] 

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) # <--- Establece la sesión (cookie)
            return Response({"detail": "Inicio de sesión exitoso."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request) # <--- Cierra la sesión (elimina la cookie)
        return Response({"detail": "Cierre de sesión exitoso."}, status=status.HTTP_200_OK)
    