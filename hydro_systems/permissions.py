from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission to only allow owners of an object to view, update or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if current logged user is the owner of the object
        return obj.owner == request.user