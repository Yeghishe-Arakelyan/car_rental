from rest_framework import permissions

class IsReservationOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission to allow owners of a reservation or staff members to access and modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a staff member
        if request.user.is_staff:
            return True

        # Check if the user is the owner of the reservation
        return obj.customer == request.user
