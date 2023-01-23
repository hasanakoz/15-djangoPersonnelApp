from rest_framework import permissions


class IsStafforReadOnly(permissions.IsAdminUser):
    message = "You don't have permission to perform this action"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
