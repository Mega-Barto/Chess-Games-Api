from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permite acceso de solo lectura para usuarios no administradores.
    Solo los administradores pueden realizar métodos de escritura.
    """

    def has_permission(self, request, view):
        # Métodos de solo lectura permitidos para todos
        if request.method in SAFE_METHODS:  # ('GET', 'HEAD', 'OPTIONS')
            return True
        # Métodos de escritura permitidos solo para administradores
        return request.user and request.user.is_staff
