from rest_framework.permissions import BasePermission

class TeacherPermission(BasePermission):

    def has_permission(self, request, view):
        groups = request.user.groups.all() 

        if groups.filter(name='Teacher').exists():
            return True
        
        return False