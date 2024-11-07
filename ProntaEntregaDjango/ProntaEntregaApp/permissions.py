from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Permiso personalizado para permitir solo a usuarios administradores (is_staff o is_superuser).
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_superuser)