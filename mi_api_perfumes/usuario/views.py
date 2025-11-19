from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserRegisterSerializer 

class RegisterView(APIView):
    # Permite acceso sin autenticación para registrar
    permission_classes = [] 
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "Registro exitoso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


