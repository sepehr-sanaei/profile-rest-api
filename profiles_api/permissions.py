from rest_framework import permissions


class UpdateOwnProfille(permissions.BasePermission):
    """Allow user to update own profile"""

    def has_object_permission(self, request, view, obj):
        """Checks user is updating their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
