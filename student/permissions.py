from rest_framework.permissions import BasePermission

class StudentPermission(BasePermission):

    def has_permission(self, request, view):
        groups = request.user.groups.all() 

        if groups.filter(name='Student').exists():
            return True
        
        return False