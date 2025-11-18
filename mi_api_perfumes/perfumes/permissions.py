from rest_framework import permissions

class ReadOnlyIfUnauthenticated(permissions.BasePermission):
    """
    Permite lectura (GET, HEAD, OPTIONS) a cualquiera, pero requiere autenticación 
    (IsAuthenticated) para la escritura (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated
    
