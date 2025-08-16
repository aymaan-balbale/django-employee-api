from rest_framework.permissions import BasePermission

class IsHRorAdminUser(BasePermission):
    """
    Allows access only to users in the HR or Admin group.
    """
    def has_permission(self, request, view):
        # Check if user is authenticated and is part of the required groups
        return request.user.is_authenticated and request.user.groups.filter(name__in=['HR', 'Admin']).exists()